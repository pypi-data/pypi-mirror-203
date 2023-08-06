from .tools import encode_json, decode_json


class ScenarioTerminatedException(Exception):
  "The scenario is ended by the user forcibly."
  pass


class ScenarioNotStartedException(Exception):
  "The scenario isn't started properly."
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
    self.bridge._send(encode_json(ij))
    res = decode_json(self.bridge._waits_for())
    self.bridge.server_socket.settimeout(None)
    if "stoken" in res:
      self.token = res["stoken"]
      self.init = True
      self._continue_scenario(j)
    elif "squeued" in res:
      while True:
        try: res = decode_json(self.bridge._waits_for())
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
    self.bridge._send(encode_json(j))

  def _terminate_scenario(self, j: dict):
    j |= {"stoken": self.token, "sfinish": True}
    self.token = None
    self.init = False
    self.nis = False
    self.bridge._send(encode_json(j))

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

  def read_cells(self, keys_arr: list, buffer_size: int = 8192):
    if not self.init or self.nis:
      return None
    j = {"memory_cells": keys_arr}
    j = decode_json(self.bridge._accept(encode_json(j), buffer_size))
    if "memory_values" not in j:
      return None
    else:
      return j["memory_values"]

  def listen(self, buffer_size: int = 8192):
    if not self.init or self.nis:
      raise ScenarioNotStartedException
    try:
      j = decode_json(self.bridge._waits_for(buffer_size))
    except UnicodeDecodeError:
      print('Unicode decode error.')
      return {}
    if "sfinish" in j:
      if j["sfinish"] is True:
        raise ScenarioTerminatedException
    return j

  def wait(self, buffer_size: int = 8192):
    while True:
      msg = self.listen(buffer_size)
      if len(msg) == 0:
        continue
      if msg['author'] == 1:
        continue
      return msg['content']

  def terminate(self):
    self._terminate_scenario(dict())
