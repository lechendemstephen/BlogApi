from fastapi import FastAPI, APIRouter, status, HTTPException

from .routers import posts, users, auth
from . import models
from .database import engine

base = models.Base.metadata.create_all(bind=engine)




app = FastAPI()


app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)


