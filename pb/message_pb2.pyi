from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Greeting(_message.Message):
    __slots__ = ["type", "content", "timestamp"]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    type: str
    content: str
    timestamp: int
    def __init__(self, type: _Optional[str] = ..., content: _Optional[str] = ..., timestamp: _Optional[int] = ...) -> None: ...
