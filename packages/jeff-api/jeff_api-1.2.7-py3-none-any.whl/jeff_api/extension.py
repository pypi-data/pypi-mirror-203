import argparse, signal
from typing import Optional
from .bridge import Bridge
from .message import Message


class ExtensionNotStartedException(Exception):
  "The extension isn't started properly."
  pass


class Extension:
  "TBD"

  def __init__(self, ext_description: str, auto_on: bool = True):
    "TBD"
    self.args_parser = argparse.ArgumentParser(description=ext_description)
    self.args_parser.add_argument("extension_port", type=int, help="extension's server port")
    self.args_parser.add_argument("jeff_port", type=int, help="Jeff port")
    self.args_parser.add_argument("-v", "--verbose", action="store_true", help="verbose output")
    self.__initialized: bool = False
    signal.signal(signal.SIGINT, self.handle_shutdown)
    signal.signal(signal.SIGTERM, self.handle_shutdown)
    if auto_on: self.turn_on('localhost', None)

  def turn_on(self, jeff_host: Optional[str] = None, extension_host: Optional[str] = None):
    "TBD"
    args = self.args_parser.parse_args()
    self.__extension_port: int = args.extension_port
    self.__jeff_port: int = args.jeff_port
    self.__verbose: bool = args.verbose
    if self.__verbose:
      print('Parsed arguments.')
    self.bridge = Bridge(jeff_host, self.__jeff_port, extension_host, self.__extension_port)
    self.__initialized = True

  def handle_shutdown(self, *args) -> None:
    "TBD"
    pass

  def handle_message(self, message: Message) -> None:
    "TBD"
    pass

  def run(self) -> None:
    "TBD"
    if not self.__initialized:
      raise ExtensionNotStartedException()
    while True:
      data = self.bridge.listen()
      if not len(data): continue
      if 'shutdown' in data:
        break
      else:
        try:
          self.handle_message(Message(data))
        except Exception as e:
          if self.__verbose:
            print(f'Handled the exception: {e}.')
    self.handle_shutdown()
