from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    password: str
    email: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    register_date: datetime

    class Config:
        orm_mode = True
