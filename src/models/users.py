from datetime import datetime
from typing import List
from pydantic import BaseModel


class UserBaseSchema(BaseModel):
    id: str | None = None
    name: str = "Administrador "
    username: str = "admin"
    password: str = "admin"
    active: bool = True
    profile_id: int = 0
    company_id: int = 0
    createdAt: datetime | None = None
    updatedAt: datetime | None = None

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True


class UpdateUserSchema(BaseModel):
    name: str
    password: str

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True


class UserResponse(BaseModel):
    status: str
    user: UserBaseSchema


class ListUserResponse(BaseModel):
    status: str
    results: int
    users: List[UserBaseSchema]
