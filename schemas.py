from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class PostBase(BaseModel):
    title : str = Field(min_length=1,max_length=100)
    content : str = Field(min_length=1)


class PostCreate(PostBase):
    pass
    

class PostResponse(PostBase):
    model_config=ConfigDict(from_attributes=True)
    id :int
    date_posted : datetime
    user_id : int
    author : UserPublic  # noqa: F821


class PostUpdate(BaseModel):
    title : str | None = Field(default=None,min_length=1,max_length=100)
    content : str | None = Field(default=None,min_length=1)

class PaginatedPostResponse(BaseModel):
    post: list[PostResponse]
    total: int
    skip: int
    limit: int
    has_more: bool



class Token(BaseModel):
    token_type : str
    access_token : str
    

class PasswordResetRequest(BaseModel):
    email: EmailStr = Field(max_length=120)


class ForgetPasswordRequest(BaseModel):
    token: str
    new_password: str = Field(min_length=8)


class ChangePasswordRequest(BaseModel):
    current_password : str
    new_password : str = Field(min_length=8)


class UserBase(BaseModel):
    username : str = Field(min_length=1,max_length=50)
    email : EmailStr= Field(max_length=120)

class UserCreate(UserBase):
    password : str = Field(min_length=8)

class UserUpdate(BaseModel):
    username: str | None = Field(default=None,min_length=1,max_length=50)
    email : EmailStr | None = Field(default=None,max_length=120)

class UserPublic(BaseModel):
    model_config=ConfigDict(from_attributes=True)
    id :int
    username : str
    image_file: str | None
    img_path : str

class UserPrivate(UserPublic):
    email : EmailStr