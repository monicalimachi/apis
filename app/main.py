
from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
app=FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts=[{"title":"title of post 1","content":"content of post 1","id":1},{"title":"favorite foods","content":"I like pizza","id":2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

def find_index_post(id):
    for i,p in enumerate(my_posts):
        if p['id']== id:
            return i

#Decorator to reference to the path and the HTTP method GET "/" the root path
@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return{"data":my_posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict=post.dict()
    post_dict['id']=randrange(0,100000)
    my_posts.append(post_dict)
    return {"data": post_dict}
#title str, content str, category, Bool published

#Order matters - the present and next functions has similar path

@app.get("/posts/latest")
def get_latest_post():
    post=my_posts[len(my_posts)-1]
    return{"detail latest":post}

@app.get("/posts/{id}")
def get_post(id:int, response:Response):
    post=find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail = f"post with {id} was not found")
        #response.status_code=status.HTTP_404_NOT_FOUND
        #return {'message': f"post with id: {id} was not found"}
    return{"post_detail": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    #deleting post 
    #find te  index in the array that has required ID
    #my_posts.pop(index)
    #204 is used to return status deleted some value
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id:int, post:Post):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"post with id: {id} does not exist")
    post_dict= post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {'data':post_dict}