import json, socket
from typing import Any, Optional
from .scenario import Scenario
from .tools import encode_json, decode_json


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
    self.scn = None
    self.init_server()

  def init_server(self) -> None:
    "TBD"
    if self.self_host is None and self.self_port is None: return
    self.self_host = self.self_host if self.self_host is not None else "0.0.0.0"
    self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.server_socket.bind((self.self_host, self.self_port))
    self.server_socket.listen()

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

  def send_msg(self, msg: str) -> None:
    "TBD"
    j = {"send": msg}
    self._send(encode_json(j))

  def send_json(self, j: dict) -> None:
    "TBD"
    self._send(encode_json(j))

  def send_as_user(self, msg: str) -> None:
    "TBD"
    j = {"send_as_user": msg}
    self._send(encode_json(j))

  def send_status(self, msg_id: str, msg: str) -> None:
    "TBD"
    j = {"send_status": {"id": msg_id, "msg": msg}}
    self._send(encode_json(j))

  def send_info(self, msg: str) -> None:
    "TBD"
    j = {"send_info": msg}
    self._send(encode_json(j))

  def send_error(self, msg: str) -> None:
    "TBD"
    j = {"send_warning": msg}
    self._send(encode_json(j))

  def store_cells(self, values_dict: dict) -> None:
    "TBD"
    j = {"store_in_memory": values_dict}
    self._send(encode_json(j))

  def read_cell(self, key: str, buffer_size: int = 8192) -> Optional[Any]:
    "TBD"
    j = {"memory_cells": [key]}
    j = decode_json(self._accept(encode_json(j), buffer_size))
    if "memory_values" not in j: return None
    if key not in j["memory_values"]: return None
    return j["memory_values"][key]

  def read_cells(self, keys_arr: list, buffer_size: int = 8192) -> Optional[list]:
    "TBD"
    j = {"memory_cells": keys_arr}
    j = decode_json(self._accept(encode_json(j), buffer_size))
    if "memory_values" not in j: return None
    return j["memory_values"]

  def listen(self) -> dict:
    "TBD"
    return decode_json(self._waits_for())

  def scenario(self, name: Optional[str]) -> Scenario:
    "TBD"
    if self.scn is None and name is not None:
      self.scn = Scenario(self, name)
    return self.scn
