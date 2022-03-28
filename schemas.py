
from datetime import date, datetime
from distutils.command.config import config
from typing import Optional
from pydantic import BaseModel, EmailStr, HttpUrl
from fastapi import UploadFile, File
# alembic==1.7.7

   
class UserData(BaseModel):
    First_Name : str
    Last_Name : str
    DOB : date
    Father_Name : str
    Matric_Marks : int
    Out_of_Matric_Marks  : int
    M_passing_year : date
    FSC_Marks : int
    Out_Of_FSC_Marks : int 
    Fsc_passing_year : date
    
class UserDataIn(UserData):
   class Config:
        orm_mode = True
   
class User(BaseModel):
    email : EmailStr

class UserOut(User):
    Id : int
    created_at : datetime
    class Config:
        orm_mode = True
    
class UserDataOut(UserData):
    Id : int
    owner_id : int
    owner : UserOut
    class Config:
        orm_mode = True

class CreateUser(User):
    password : str  



class Token(BaseModel):
    access_token : str
    token_type : str 
    
    class Config:
        orm_mode = True

class TokenData(BaseModel):
    id : Optional[str] = None
    