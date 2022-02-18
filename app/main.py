from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user , auth
from .config import Settings

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

#Decorator to reference to the path and the HTTP method GET "/" the root path
@app.get("/")
def root():
    return {"message": "Hello World"}

