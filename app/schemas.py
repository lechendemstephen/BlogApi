from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime

class Posts(BaseModel): 
    title: str 
    description: str
   
class PostsOut(Posts): 
    id: int
    created_at: datetime
    owner_id: int

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

class TOkenData(BaseModel): 
    id: Optional[str] = None