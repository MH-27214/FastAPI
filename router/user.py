from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from db.database import get_db
from schemas import UserBase, UserDisplay
from db import db_user
from typing import List

router = APIRouter(
    prefix="/users",
    tags=["user"],
)

#creat user
@router.post("/",response_model=UserDisplay)
async def create_user(request: UserBase,db:Session =Depends(get_db)):
    return db_user.create_user(db,request)

#read all user
@router.get("/",response_model=List[UserDisplay])
async def get_all_users(db:Session = Depends(get_db)):
    return db_user.get_all_users(db)

#read one user
@router.get("/{id}",response_model=UserDisplay)
async def get_user(id:int,db:Session = Depends(get_db)):
    return db_user.get_user(db,id)

#update user
@router.post("/{id}/update")
async def update_user(id:int,request:UserBase,db:Session = Depends(get_db)):
    return db_user.update_user(db,id,request)
#delete user
@router.get("/delete/{id}")
async def delete_user(id:int,db:Session = Depends(get_db)):
    return db_user.delete_user(db,id)
