import json, socket
from typing import Any, Optional
from .tools import encode_json, decode_json


class ScenarioNotStartedException(Exception):
  "The scenario isn't started properly."
  pass


class ScenarioStates:
  "Contains scenario states."
  UNUSED = 0
  NOT_STARTED = 1
  STARTED = 2
  PREFINISHED = 3


class Bridge:
  "TBD"

  def __init__(
    self,
    jeff_host: Optional[str],
    jeff_port: int,
    self_host: Optional[str] = None,
    self_port: Optional[int] = None
  ):
    "TBD"
    self.jeff_host = jeff_host
    self.jeff_port = jeff_port
    self.self_host = self_host
    self.self_port = self_port
    self.shutdown_requested = False
    self.__scenario_status: int = ScenarioStates.UNUSED
    self.__scenario_token: Optional[str] = None
    self.__scenario_name: Optional[str] = None
    self.init_server()

  def init_server(self) -> None:
    "TBD"
    if self.self_host is None and self.self_port is None: return
    self.self_host = self.self_host if self.self_host is not None else "0.0.0.0"
    self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.server_socket.bind((self.self_host, self.self_port))
    self.server_socket.listen()

  def __del__(self):
    self.server_socket.close()
    del self.server_socket

  def _send(self, data: bytes) -> None:
    "TBD"
    try:
      with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((self.jeff_host, self.jeff_port))
        sock.sendall(data)
    except ConnectionRefusedError:
      print('Jeff\'s socket is disabled.')

  def _accept(self, data: bytes, buffer_size: int) -> bytes:
    "TBD"
    try:
      with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((self.jeff_host, self.jeff_port))
        sock.sendall(data)
        data = sock.recv(buffer_size)
        while not len(data):
          data = sock.recv(buffer_size)
    except ConnectionRefusedError:
      print('Jeff\'s socket is disabled.')
    return data

  def _waits_for(self, buffer_size: int = 8192) -> bytes:
    "TBD"
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

  def _init_scenario(self, j: dict) -> None:
    "TBD"
    self.server_socket.settimeout(5)
    ij = {
      "sready": True,
      "saddr": self.self_host,
      "sport": self.self_port,
      "sname": self.name
    }
    self._send(encode_json(ij))
    res = decode_json(self._waits_for())
    self.server_socket.settimeout(None)
    if "stoken" in res:
      self.__scenario_token = res["stoken"]
      self.__scenario_status = ScenarioStates.STARTED
      self._continue_scenario(j)
    elif "squeued" in res:
      while True:
        try: res = decode_json(self._waits_for())
        except UnicodeDecodeError: print('Unicode decode error.')
        if "stoken" not in res: raise ScenarioNotStartedException
        self.__scenario_token = res["stoken"]
        self.__scenario_status = ScenarioStates.STARTED
        self._continue_scenario(j)
        break
    else:
      raise ScenarioNotStartedException

  def _continue_scenario(self, j: dict) -> None:
    "TBD"
    j |= {"stoken": self.__scenario_token, "scontinue": True}
    self._send(encode_json(j))

  def _terminate_scenario(self, j: dict) -> None:
    "TBD"
    j |= {"stoken": self.__scenario_token, "sfinish": True}
    self._send(encode_json(j))

  def _decide(
    self,
    j: dict,
    is_last_message_for_scenario: bool
  ) -> None:
    "TBD"
    if is_last_message_for_scenario and self.__scenario_status != ScenarioStates.UNUSED:
      self.__scenario_status = ScenarioStates.PREFINISHED
    if self.__scenario_status == ScenarioStates.UNUSED:
      self._send(encode_json(j))
    elif self.__scenario_status == ScenarioStates.NOT_STARTED:
      self._init_scenario(j)
      self.__scenario_status = ScenarioStates.STARTED
    elif self.__scenario_status == ScenarioStates.STARTED:
      self._continue_scenario(j)
    elif self.__scenario_status == ScenarioStates.PREFINISHED:
      self._terminate_scenario(j)
      self.__scenario_status = ScenarioStates.UNUSED

  def send_json(
    self,
    j: dict,
    is_last_message_for_scenario: bool = False
  ) -> None:
    "TBD"
    self._decide(j, is_last_message_for_scenario)

  def send_msg(
    self,
    msg: str,
    is_last_message_for_scenario: bool = False
  ) -> None:
    "TBD"
    j = {"send": msg}
    self._decide(j, is_last_message_for_scenario)

  def send_as_user(
    self,
    msg: str,
    is_last_message_for_scenario: bool = False
  ) -> None:
    "TBD"
    j = {"send_as_user": msg}
    self._decide(j, is_last_message_for_scenario)

  def send_status(
    self,
    msg_id: str,
    msg: str,
    is_last_message_for_scenario: bool = False
  ) -> None:
    "TBD"
    j = {"send_status": {"id": msg_id, "msg": msg}}
    self._decide(j, is_last_message_for_scenario)

  def send_info(
    self,
    msg: str,
    is_last_message_for_scenario: bool = False
  ) -> None:
    "TBD"
    j = {"send_info": msg}
    self._decide(j, is_last_message_for_scenario)

  def send_error(
    self,
    msg: str,
    is_last_message_for_scenario: bool = False
  ) -> None:
    "TBD"
    j = {"send_warning": msg}
    self._decide(j, is_last_message_for_scenario)

  def store_cells(
    self,
    values_dict: dict,
    is_last_message_for_scenario: bool = False
  ) -> None:
    "TBD"
    j = {"store_in_memory": values_dict}
    self._decide(j, is_last_message_for_scenario)

  def read_cell(
    self,
    key: str,
    buffer_size: int = 8192,
    is_last_message_for_scenario: bool = False
  ) -> Optional[Any]:
    "TBD"
    j = {"memory_cells": [key]}
    j = decode_json(self._accept(encode_json(j), buffer_size))
    if "memory_values" not in j: return None
    if key not in j["memory_values"]: return None
    return j["memory_values"][key]

  def read_cells(
    self,
    keys_arr: list,
    buffer_size: int = 8192,
    is_last_message_for_scenario: bool = False
  ) -> Optional[list]:
    "TBD"
    j = {"memory_cells": keys_arr}
    j = decode_json(self._accept(encode_json(j), buffer_size))
    if "memory_values" not in j: return None
    return j["memory_values"]

  def listen(self, buffer_size: int = 8192) -> dict:
    "TBD"
    if self.__scenario_status == ScenarioStates.UNUSED:
      return decode_json(self._waits_for(buffer_size))
    elif self.__scenario_status == ScenarioStates.STARTED:
      j: Any = dict()
      try:
        j = decode_json(self.bridge._waits_for(buffer_size))
      except UnicodeDecodeError:
        print('Unicode decode error.')
        return j
      if "sfinish" in j:
        if j["sfinish"] is True:
          self.__scenario_status = ScenarioStates.UNUSED
      return j

  def wait(self, buffer_size: int = 8192) -> Optional[str]:
    "TBD"
    if self.__scenario_status != ScenarioStates.STARTED:
      return
    while True:
      msg = self.listen(buffer_size)
      if len(msg) == 0:
        continue
      if msg['author'] == 1:
        continue
      return msg['content']

  def scenario(self, name: Optional[str]) -> bool:
    "TBD"
    if self.__scenario_status == ScenarioStates.UNUSED and name is not None:
      self.__scenario_status = ScenarioStates.NOT_STARTED
      self.__scenario_name = name
      return True
    else:
      return False

  def terminate_scenario(self) -> None:
    "TBD"
    self._terminate_scenario(dict())
    self.__scenario_token = None
    self.__scenario_name = None
    self.__scenario_status = ScenarioStates.UNUSED
