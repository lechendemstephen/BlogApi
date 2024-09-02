from pydantic import BaseModel, EmailStr


class Posts(BaseModel): 
    title: str 
    description: str

class UpdatePosts(Posts): 
    pass 

class Users(BaseModel): 
    email: EmailStr
    password: str

class UsersOut(BaseModel): 
    name: str
    email: str

class Login(BaseModel):
    email: EmailStr
    password: str