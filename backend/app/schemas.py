from datetime import datetime
from typing import List
from pydantic import BaseModel, EmailStr, constr
from bson.objectid import ObjectId


class UserBaseSchema(BaseModel):
    name: str
    email: str
    photo: str | None
    role: str | None
    created_at: datetime | None
    updated_at: datetime | None

    class Config:
        orm_model = True


class CreateUserSchema(UserBaseSchema):
    password: constr(min_length=8)
    passwordConfirm: str
    verified: bool = True


class LoginUserSchema(BaseModel):
    email: EmailStr
    password: constr(min_length=8)


class UserResponseSchema(UserBaseSchema):
    id: str
    pass


class UserResponse(BaseModel):
    status: str
    user: UserResponseSchema


class FilteredUserResponse(UserBaseSchema):
    id: str


class PostBaseSchema(BaseModel):
    title: str
    content: str
    category: str
    image: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_model = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class CreatePostSchema(PostBaseSchema):
    user: ObjectId
    pass


class PostResponse(PostBaseSchema):
    id: str
    user: FilteredUserResponse
    created_at: datetime
    updated_at: datetime


class UpdatePostSchema(BaseModel):
    title: str
    content: str
    category: str
    image: str
    user: str

    class Config:
        orm_model = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class ListPostResponse(BaseModel):
    status: str
    result: int
    posts: List[PostResponse]
