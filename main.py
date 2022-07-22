from fastapi import FastAPI

from api import users
from db.db_setup import engine
from db.models import user

user.Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="User Data Storage",
    description="Simple service for storing user's data"
)

app.include_router(users.router)
