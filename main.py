from fastapi import FastAPI
from routes.teacher import router as teacher_router
from routes.common import router as common_router
from routes.job import router as job_router
from routes.auth import router as auth_router
from routes.user import router as users_router
from models.teachers import * 
from models.teacher_utils import *
from models.common import *
from models.job import *
from sqlalchemy.orm import Session
from db import engine, get_db, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(teacher_router)
app.include_router(job_router)
app.include_router(common_router)

@app.get("/")
def read_root():
    return {"message": "welcome to the tuition project backend!"}