import json
from typing import Any


def encode_json(j: dict) -> bytes:
  "TBD"
  return json.dumps(j).encode()


def decode_json(b: bytes) -> Any:
  "TBD"
  return json.loads(b.decode())
