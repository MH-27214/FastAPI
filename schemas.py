from pydantic import BaseModel
from typing import List

class UserBase(BaseModel):
    username: str
    email: str
    password: str
class UserDisplay(BaseModel):
    username: str
    email: str
    class Config():
        orm_mode = True

# user inside article display
class User(BaseModel):
    id:int
    username: str

class Comment(BaseModel):
    id: int
    content: str

class Post(BaseModel):
    id: int
    content: str
    comments: List[Comment] = []
