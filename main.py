
from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
app=FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

#Decorator to reference to the path and the HTTP method GET "/" the root path
@app.get("/")
def root():
    return {"message": "Welcome to my api!!!"}

@app.get("/posts")
def get_posts():
    return{"data":"This is your posts"}


@app.post("/createposts")
def create_posts(post: Post):
    print(post)
    print(post.dict())
    return {"data": "post"}
#title str, content str, category, Bool published
