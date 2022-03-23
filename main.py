from fastapi import FastAPI, Depends, HTTPException
import Routers.userdata, Routers.user, Routers.Auth
from database import get_db
# from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get('/')
async def root():
    return {"FastAPI":"Hello World"}


app.include_router(Routers.userdata.router)
app.include_router(Routers.user.router)
app.include_router(Routers.Auth.router)

