from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import engine
from .routers import post, user , auth, vote
from .config import Settings

#You can remove this if you use Alembic to autoenerate databases
#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Configure Strict domains that can reach apis, add domain example "https://www.google.com"
origins=["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

#Decorator to reference to the path and the HTTP method GET "/" the root path
@app.get("/",status_code=status.HTTP_200_OK)
def root():
    return {"message": "Hello World"}

