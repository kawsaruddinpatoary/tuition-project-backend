from fastapi import FastAPI
from routes.teacher import router as teacher_router
from routes.common import router as common_router
from models.teachers import * 
from models.teacher_utils import *
from models.common import *
from sqlalchemy.orm import Session
from db import engine, get_db, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(teacher_router)
app.include_router(common_router)
@app.get("/")
def read_root():
    return {"message": "welcome to the tuition project backend!"}