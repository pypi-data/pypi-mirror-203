from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetNotificationInfoRequest(_message.Message):
    __slots__ = ["id", "service_token"]
    ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    id: str
    service_token: str
    def __init__(self, service_token: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class GetNotificationInfoResponse(_message.Message):
    __slots__ = ["email", "id"]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    email: str
    id: str
    def __init__(self, id: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...
