

from os import access
from fastapi import APIRouter, HTTPException,status, Depends

import models, utils, Oauth2
from database import get_db

import schemas
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from typing import List
router = APIRouter()
@router.post('/login', response_model= schemas.Token)
async def Login(user_credintials: OAuth2PasswordRequestForm = Depends(), db : Session= Depends(get_db)):
    print("I am Login Function")
    user = db.query(models.User).filter(models.User.email == user_credintials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user at this {user_credintials.username} email dose not exist")
    if not utils.verify(user_credintials.password , user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"wrong Password Please Try Again")
    access_token  = Oauth2.create_access_token(data= {"user_id" : user.Id})
    print("access_token", access_token)
    # return access_token
    return {"access_token":access_token , "token_type" : "Barear"}

