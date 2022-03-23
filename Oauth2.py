from datetime import datetime, timedelta
from statistics import mode
from fastapi import Depends, status, HTTPException
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
import schemas, database, models

from sqlalchemy.orm import Session
from config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = 'login')

def create_access_token(data : dict):
    print("I am create access token")
    to_encode = data.copy()
    expire = datetime.utcnow()+timedelta(minutes=settings.acess_token_expire_minutes)
    to_encode.update({"exp": expire})

    encode_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
    print(encode_jwt)
    return encode_jwt 

def verify_access_token(token : str, credentials_exception):
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        id : str = payload.get("user_id")
        if id is None:
            raise credentials_exception
        token_data = schemas.TokenData(id=id)
    except JWTError:
        raise credentials_exception
    return token_data

def get_current_user(token : str = Depends(oauth2_scheme), db : Session = Depends(database.get_db)):
    print("Token : ", token)
    credentials_exception = HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials", headers={"WWW-Authenticate" : "Bearer"})
    token = verify_access_token(token, credentials_exception)
    user = db.query(models.User).filter(models.User.Id == token.id).first()

    return user


