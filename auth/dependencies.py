from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from .utils import verify_password, get_password_hash, create_access_token, SECRET_KEY, ALGORITHM
from schemas.auth import TokenData
from models.user import User
from db import SessionLocal, engine, Base


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_user(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def authenticate_user(db: Session, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    # 1. Step: Purely decode the JWT String and handle expiration safely
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        token_type: str = payload.get("type")
        if username is None or token_type != "access":
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    # 2. Step: Instantiate your validation model safely OUTSIDE the try/except block 
    # to catch any hidden Pydantic validation issues if they exist
    token_data = TokenData(username=username)

    # 3. Step: Validate Database Entry presence
    user = get_user(db, username=token_data.username)
    if user is None:
        # If the user is missing from the DB or named differently, raise explicit error to clarify
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Token valid, but user '{token_data.username}' does not exist in database."
        )
        
    return user