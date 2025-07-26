from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from core.auth import get_current_user
from models.user import User
from schemas.user import UserResponse

router = APIRouter(prefix="/users", tags=["Users"])


# Getting all users
@router.get("/", response_model=List[UserResponse])
async def get_all_users(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    users = db.query(User).all()
    return users


# Getting user by ID
@router.get("/{user_id}", response_model=UserResponse)
async def get_user_by_id(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
