from pydantic import BaseModel
from datetime import datetime
from typing import Annotated, Literal, Union

class User(BaseModel):
    sid: int
    first_name: str
    last_name: str | None = None
    dob: datetime
    gender: Literal["MALE"] | Literal["FEMALE"] | Literal["OTHER"]
    bio: str | None = None

class UserUpdate(BaseModel):
    sid: int | None = None
    first_name: str | None = None
    last_name: str | None = None
    dob: datetime | None = None
    gender: Literal["MALE"] | Literal["FEMALE"] | Literal["OTHER"] | None = None
    bio: str | None = None