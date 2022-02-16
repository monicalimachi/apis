from distutils.log import error
from logging import exception
from pydoc import ModuleScanner
from typing import Optional, List
from fastapi import Depends, FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models, schemas, utils
from .database import engine, get_db
from .routers import post, user , auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()



#Connection to DB postgresql developer server
while True:

    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', port=15432, user = 'dulcinea', password='root', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was succesfull!")
        break
    except Exception as error:
        print ("Connecting to database failed")
        print("Error: ", error)
        time.sleep(2)

my_posts=[{"title":"title of post 1","content":"content of post 1","id":1},{"title":"favorite foods","content":"I like pizza","id":2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

def find_index_post(id):
    for i,p in enumerate(my_posts):
        if p['id']== id:
            return i


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

#Decorator to reference to the path and the HTTP method GET "/" the root path
@app.get("/")
def root():
    return {"message": "Hello World"}

