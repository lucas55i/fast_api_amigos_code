from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum


class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    admin = "admin"
    user= "user"
    student  = "student"

class User(BaseModel):
    id:  Optional[UUID] =  uuid4()
    fisrt_name: str
    last_name: str
    middle_name: Optional[str]
    gender: Gender
    roles: List[Role]

class  UserUpdateRequest(BaseModel):
    def __init__(__pydantic_self__, **data: Any):
        super().__init__(data)
        __pydantic_self__.first_name = None

    fisrt_name: Optional[str]
    last_name: Optional[str]
    middle_name: Optional[str]
    roles: Optional[List[Role]]