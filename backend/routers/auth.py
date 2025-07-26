from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
import os
from dotenv import load_dotenv

from database import get_db
from core.auth import authenticate_user, create_access_token, get_password_hash
from models.user import User
from schemas.user import UserCreate, UserLogin, Token

# Load environment variables
load_dotenv()
ACCESS_TOKEN_EXPIRE_MINUTE = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTE", "30"))

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/signup")
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if username already exists
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        return JSONResponse(
            status_code=400,
            content={"message": "Username already taken"}
        )
    
    # Create new user
    hashed_password = get_password_hash(user.password)
    db_user = User(
        username=user.username,
        hashedpassword=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return JSONResponse(
        status_code=201,
        content={"message": f"User created successfully with username: {user.username}"}
    )

@router.post("/login", response_model=Token)
async def login_with_json(user_login: UserLogin, db: Session = Depends(get_db)):
    """
    Login with username and password
    """
    user = authenticate_user(user_login.username, user_login.password, db)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password"
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTE)
    access_token = create_access_token(
        data={"id": user.id}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/login-oauth2", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """
    OAuth2 compatible login (for Swagger UI authorization)
    """
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTE)
    access_token = create_access_token(
        data={"id": user.id}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
