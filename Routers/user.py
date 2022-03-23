from asyncio import run_coroutine_threadsafe
from re import A
from fastapi import FastAPI, status, Depends, APIRouter

import models, schemas, utils

from database import get_db
from sqlalchemy.orm import Session
from typing import List

router = APIRouter()

@router.post('/create_user' , response_model= schemas.UserOut)

async def CreateUser(user : schemas.CreateUser , db : Session = Depends(get_db)):
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/AllUsers', response_model=List[schemas.UserOut])
async def  GetUsers(db : Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users