from pydantic import BaseModel
from typing import Union


class User(BaseModel):
    id: Union[str, None] = None
    username: str
    hashed_password: str
    phone: str
    email: str


class UserInDB(User):
    hashed_password: str
