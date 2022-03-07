from basic_auth.routers import item, user, authentication
from fastapi import FastAPI
from basic_auth import models
from basic_auth.database import engine

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(item.router)
app.include_router(user.router)
