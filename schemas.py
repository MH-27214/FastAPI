from pydantic import BaseModel

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

