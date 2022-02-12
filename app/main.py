
from distutils.log import error
from logging import exception
from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time

app=FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    #rating: Optional[int] = None

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

#Decorator to reference to the path and the HTTP method GET "/" the root path
@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts """)
    posts = cursor.fetchall()
    print(posts)
    return{"data":posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    cursor.execute("""INSERT INTO posts (title,content,published) VALUES (%s,%s,%s) RETURNING * 
    """,(post.title, post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit()
    return {"data": new_post}
#title str, content str, category, Bool published

#Order matters - the present and next functions has similar path

@app.get("/posts/latest")
def get_latest_post():
    post=my_posts[len(my_posts)-1]
    return{"detail latest":post}

@app.get("/posts/{id}")
def get_post(id:int, response:Response):
    cursor.execute("""SELECT * from posts WHERE id = %s""", (str(id),))
    post = cursor.fetchone()
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
    cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING * """, (str(id)))
    deleted_post = cursor.fetchone()
    conn.commit()
    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id:int, post:Post):
    cursor.execute("""UPDATE posts SET title = %s, content= %s, published = %s WHERE id = %s RETURNING *""",
    (post.title, post.content, post.published, (str(id))))
    updated_post = cursor.fetchone()
    conn.commit()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"post with id: {id} does not exist")
    return {'data':updated_post}