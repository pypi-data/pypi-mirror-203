import json, socket
from typing import Optional


class ScenarioTerminatedException(Exception):
  "The scenario is ended by the user forcibly."
  pass


class ScenarioNotStartedException(Exception):
  "The scenario is ended by the user forcibly."
  pass


class Scenario:
  "TBD"

  def __init__(self, bridge, name=None):
    self.bridge = bridge
    self.init = False
    self.token = None
    self.nis = False
    if not name:
      self.name = f'Scenario at {self.bridge.self_host}:{self.bridge.self_port}'
    else:
      self.name = name

  def _init_scenario(self, j: dict):
    self.bridge.server_socket.settimeout(5)
    ij = {"sready": True, "saddr": self.bridge.self_host, "sport": self.bridge.self_port, "sname": self.name}
    self.bridge._send(Bridge._encode_json(ij))
    res = Bridge._decode_json(self.bridge._waits_for())
    self.bridge.server_socket.settimeout(None)
    if "stoken" in res:
      self.token = res["stoken"]
      self.init = True
      self._continue_scenario(j)
    elif "squeued" in res:
      while True:
        try: res = Bridge._decode_json(self.bridge._waits_for())
        except UnicodeDecodeError: print('Unicode decode error.')
        if "stoken" not in res: raise ScenarioNotStartedException
        self.token = res["stoken"]
        self.init = True
        self._continue_scenario(j)
        break
    else:
      raise ScenarioNotStartedException

  def _continue_scenario(self, j: dict):
    j |= {"stoken": self.token, "scontinue": True}
    self.bridge._send(Bridge._encode_json(j))

  def _terminate_scenario(self, j: dict):
    j |= {"stoken": self.token, "sfinish": True}
    self.token = None
    self.init = False
    self.nis = False
    self.bridge._send(Bridge._encode_json(j))

  def _decide(self, j: dict):
    if self.nis:
      self._terminate_scenario(j)
    elif self.init:
      self._continue_scenario(j)
    else:
      self._init_scenario(j)

  def send_msg(self, msg: str, last=False):
    if last:
      self.nis = True
    j = {"send": msg}
    self._decide(j)

  def send_as_user(self, msg: str, last=False):
    if last:
      self.nis = True
    j = {"send_as_user": msg}
    self._decide(j)

  def send_status(self, msg_id: str, msg: str, last=False):
    if last:
      self.nis = True
    j = {"send_status": {"id": msg_id, "msg": msg}}
    self._decide(j)

  def send_info(self, msg: str, last=False):
    if last:
      self.nis = True
    j = {"send_info": msg}
    self._decide(j)

  def send_error(self, msg: str, last=False):
    if last:
      self.nis = True
    j = {"send_warning": msg}
    self._decide(j)

  def store_cells(self, values_dict: dict, last=False):
    if last:
      self.nis = True
    j = {"store_in_memory": values_dict}
    self._decide(j)

  def read_cells(self, keys_arr: list, buffer_size=8192):
    if not self.init or self.nis:
      return None
    j = {"memory_cells": keys_arr}
    j = Bridge._decode_json(self.bridge._accept(Bridge._encode_json(j), buffer_size))
    if "memory_values" not in j:
      return None
    else:
      return j["memory_values"]

  def listen(self, buffer_size=8192):
    if not self.init or self.nis:
      raise ScenarioNotStartedException
    try:
      j = Bridge._decode_json(self.bridge._waits_for(buffer_size))
    except UnicodeDecodeError:
      print('Unicode decode error.')
      return {}
    if "sfinish" in j:
      if j["sfinish"] is True:
        raise ScenarioTerminatedException
    return j

  def wait(self, buffer_size=8192):
    while True:
      msg = self.listen(buffer_size)
      if len(msg) == 0:
        continue
      if msg['author'] == 1:
        continue
      return msg['content']

  def terminate(self):
    self._terminate_scenario(dict())


class Bridge:
  "TBD"

  def __init__(self, jeff_host: Optional[str], jeff_port: int, self_host: Optional[str], self_port: int):
    self.jeff_host = jeff_host
    self.jeff_port = jeff_port
    self.self_host = self_host if self_host is not None else "0.0.0.0"
    self.self_port = self_port
    self.init_server()

  def init_server(self):
    self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.server_socket.bind((self.host, self.port))
    self.server_socket.listen()

  def _encode_json(j: dict):
    return json.dumps(j).encode()

  def _decode_json(b: bytes):
    return json.loads(b.decode())

  def _send(self, data: bytes):
    try:
      with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((self.ip, self.socket_port))
        sock.sendall(data)
    except ConnectionRefusedError:
      print('Jeff\'s socket is disabled.')

  def _accept(self, data: bytes, buffer_size: int):
    try:
      with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((self.ip, self.socket_port))
        sock.sendall(data)
        data = sock.recv(buffer_size)
        while not len(data):
          data = sock.recv(buffer_size)
    except ConnectionRefusedError:
      print('Jeff\'s socket is disabled.')
    return data

  def _waits_for(self, buffer_size=8192):
    try:
      (socket, address) = self.server_socket.accept()
      data = socket.recv(buffer_size)
      socket.close()
      return data
    except ConnectionRefusedError:
      print("Connection refused.")
      return b"{}"
    except json.decoder.JSONDecodeError:
      print('JSON decode error.')
      return b"{}"

  def send_msg(self, msg: str):
    j = {"send": msg}
    self._send(Bridge._encode_json(j))

  def send_json(self, j: dict):
    self._send(Bridge._encode_json(j))

  def send_as_user(self, msg: str):
    j = {"send_as_user": msg}
    self._send(Bridge._encode_json(j))

  def send_status(self, msg_id: str, msg: str):
    j = {"send_status": {"id": msg_id, "msg": msg}}
    self._send(Bridge._encode_json(j))

  def send_info(self, msg: str):
    j = {"send_info": msg}
    self._send(Bridge._encode_json(j))

  def send_error(self, msg: str):
    j = {"send_warning": msg}
    self._send(Bridge._encode_json(j))

  def store_cells(self, values_dict: dict):
    j = {"store_in_memory": values_dict}
    self._send(Bridge._encode_json(j))

  def read_cell(self, key: str, buffer_size=8192):
    j = {"memory_cells": [key]}
    j = Bridge._decode_json(self._accept(Bridge._encode_json(j), buffer_size))
    if "memory_values" not in j: return None
    if key not in j["memory_values"]: return None
    return j["memory_values"][key]

  def read_cells(self, keys_arr: list, buffer_size=8192):
    j = {"memory_cells": keys_arr}
    j = Bridge._decode_json(self._accept(Bridge._encode_json(j), buffer_size))
    if "memory_values" not in j: return None
    return j["memory_values"]

  def listen(self):
    return Bridge._decode_json(self._waits_for())

  def scenario(self, name: Optional[str]):
    if self.scn is None and name is not None:
      self.scn = Scenario(self, name)
    return self.scn
