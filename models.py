from datetime import date, datetime
from sqlalchemy import Column, Integer, String, true,ForeignKey
from database import Base
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
# from uuid import uuid4
from sqlalchemy.orm import relationship



class UserData(Base):
    __tablename__ = "userdata"
    Id = Column(Integer ,primary_key=True , index= True)
    First_Name = Column(String , nullable=False)
    Last_Name = Column(String , nullable=False)
    DOB = Column(String, nullable=False) 
    Father_Name = Column(String , nullable=False)
    Matric_Marks = Column(Integer, nullable=False)
    Out_of_Matric_Marks = Column(Integer, nullable=False)
    M_passing_year = Column(String, nullable=False) 
    FSC_Marks = Column(Integer, nullable=False)
    Out_Of_FSC_Marks = Column(Integer, nullable=False)
    Fsc_passing_year = Column(String, nullable=False) 
    created_at = Column(TIMESTAMP(timezone=True) , nullable = False, server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey("user.Id", ondelete="CASCADE"), nullable=False)
    owner = relationship("User")
    
# class UserImage(Base):
#     __tablename__  ="userimage"
#     Id = Column(Integer,primary_key = True)
#     name = Column(String, nullable=False)
#     type = Column(String, nullable=False)

class User(Base):
    __tablename__ = "user"
    Id = Column(Integer,primary_key = True)
    email = Column(String , nullable= False)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False, server_default = text('now()')) 