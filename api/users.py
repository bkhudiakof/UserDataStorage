from typing import List

import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

from db.db_setup import async_get_db, get_db
from pydantic_schemas.user import UserCreate, User
from api.utils.users import get_user, get_user_by_email, get_users, create_user

router = fastapi.APIRouter()


@router.post("/user", response_model=User, status_code=201)
async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=400, detail="This email is already registered"
        )
    return create_user(db=db, user=user)


@router.get("/user/{user_id}", response_model=User)
async def read_user(user_id: int, db: AsyncSession = Depends(async_get_db)):
    db_user = await get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


# @router.put("/user/{user_id}", response_model=User)
# async def


@router.patch("/user/{user_id}")
async def update_user():
    return {"user": []}


# @router.delete("/user/{user_id}/", status_code=200)
# async def delete_user(user_id: int, db: AsyncSession = Depends(async_get_db)):
    

@router.get("/user-list", response_model=List[User])
async def read_users(
        skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    users = get_users(db, skip=skip, limit=limit)
    return users
