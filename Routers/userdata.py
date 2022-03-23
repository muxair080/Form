from fastapi import APIRouter, Depends, HTTPException, status,Response
from sqlalchemy.orm import Session
import schemas ,models
from typing import List
from database import get_db
router = APIRouter()
from Oauth2 import get_current_user
@router.post('/userdata', response_model= schemas.UserDataOut)
def EnterData(new_user : schemas.UserDataIn, db :Session = Depends(get_db), current_user : int = Depends(get_current_user)):
    print('current_user' , current_user.email)
    data = models.UserData(owner_id = current_user.Id, **new_user.dict())
    # print('Data.owner_id' , data.owner_id)
    db.add(data)
    db.commit()
    db.refresh(data)
    return data

@router.get('/user/{id}')
def SingleUser(id : int, db : Session  = Depends(get_db), current_user : int = Depends(get_current_user)):
    print("user data function")
    user_data = db.query(models.UserData).filter(models.UserData.Id == id).all()
    
    print("user_data",user_data)
    if not user_data:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT , detail="data not found")
    
    return user_data

@router.get('/users', response_model= List[schemas.UserDataOut])
async def AllUsers(db: Session = Depends(get_db), current_user : int = Depends(get_current_user)):
    users = db.query(models.UserData).all()
    return users

@router.put('/updateuser/{id}', response_model= schemas.UserDataOut)
async def UpdateUserData(id : int, new_data : schemas.UserDataIn , db : Session = Depends(get_db),current_user : int = Depends(get_current_user)):
    data = db.query(models.UserData).filter(models.UserData.Id == id)
    userdata = data.first()

    if not userdata:
      raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f'user at this {id} id not found')
    
    if userdata.owner_id != current_user.Id:
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, detail=f'UNAUTHORIZED user')
    
    data.update(new_data.dict(), synchronize_session=False)
    db.commit()

    return data.first()

@router.delete('/delete/{id}')
async def DeleteData(id : int, db : Session = Depends(get_db),current_user : int = Depends(get_current_user)):
    user_data  = db.query(models.UserData).filter(models.UserData.Id == id)
    user = user_data.first()
    print("User : ",user)
    if not user:
        print("User dose not exist")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f'user at this {id} id not found')
    
    if user.owner_id != current_user.Id:
          raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail=f'unauthorized user')

    user_data.delete(synchronize_session=False)
    db.commit()
    Response(status_code=status.HTTP_204_NO_CONTENT)

@router.get('/allusersdata', response_model=List[schemas.UserDataOut])
async def AllUsersData(db : Session = Depends(get_db)):
    usersdata = db.query(models.UserData).all()
    print("usersdata : ",usersdata)
    return usersdata