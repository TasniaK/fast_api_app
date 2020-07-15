# # pydantic models i.e. schemas/searialisers

from typing import List, Optional

from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None


# class TaskCreate(TaskBase):
#     pass


# class Task(TaskBase):
#     id: int
#     done: bool
#     owner_id: int

#     class Config:
#         # adds compatibility with orms (trys data.id as well as data['id'])
#         orm_mode = True


# class UserBase(BaseModel):
#     email: str


# class UserCreate(UserBase):
#     # password required on user creation
#     password: str


# class User(UserBase):
#     # password not part of User schema as it won't ever be returned via API.
#     id: int
#     is_active: bool
#     tasks: List[Task] = []

#     class Config:
#         orm_mode = True

