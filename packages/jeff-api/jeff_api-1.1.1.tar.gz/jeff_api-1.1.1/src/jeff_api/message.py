class Message:
  "TBD"
  # Making some constants:
  #   1. For `author` message field.
  A_SOMEONE = 0
  A_JEFF = 1
  A_USER = 2
  #   2. For `content_type` message field.
  CT_SOMEWHAT = 0
  CT_PLAIN_TEXT = 1
  CT_MARKDOWN = 2
  CT_PICTURE = 3
  CT_FILE = 4

  def __init__(self, data: dict):
    "TBD"
    self.author: int = data['author']
    self.content_type: int = data['content_type']
    self.content: str = data['content']
    self.datetime: str = data['datetime']
