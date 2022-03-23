
from datetime import datetime
from distutils.command.config import config
import email
from typing import Optional
from pydantic import BaseModel, EmailStr





class UserData(BaseModel):
    First_Name : str
    Last_Name : str
    Father_Name : str
    Matric_Marks : int
    Out_of_Matric_Marks  : int
    FSC_Marks : int
    Out_Of_FSC_Marks : int 

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
    