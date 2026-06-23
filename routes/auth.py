from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from auth.dependencies import get_db, authenticate_user, get_user
from auth.utils import ALGORITHM, SECRET_KEY, create_access_token, create_refresh_token 
from models.common import Roles
from models.teachers import Teacher
from schemas.auth import Token, TokenRefreshRequest
from schemas.auth import UserCreate
from models.user import User
from auth.utils import get_password_hash
from jose import jwt, JWTError

from schemas.user import UserRegisterRequest

router = APIRouter()

@router.post("/login", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    refresh_token = create_refresh_token(data={"sub": user.username})
    
    return {
        "access_token": access_token, 
        "refresh_token": refresh_token, 
        "token_type": "bearer"
    }


@router.post("/register")
def register_user(user_data: UserRegisterRequest, db: Session = Depends(get_db)):
    existing_user = get_user(db, username=user_data.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")
        
    target_role = db.query(Roles).filter(Roles.id == user_data.role_id).first()
    if not target_role:
        raise HTTPException(status_code=400, detail="The assigned role ID is invalid.")
    
    hashed_pwd = get_password_hash(user_data.password)
    new_user = User(
        username=user_data.username,
        name=user_data.name,
        email=user_data.email,
        hashed_password=hashed_pwd,
        role_id=user_data.role_id
    )
    
    db.add(new_user)
    db.flush() # Flushes record to generate new_user.id without finalizing transaction yet
    
    # 4. Check if the assigned role requires profile expansion
    if target_role.role.lower() == "teacher":
        # Check if email is already taken in the teacher space to prevent collisions
        existing_teacher = db.query(Teacher).filter(Teacher.email == user_data.email).first()
        if existing_teacher:
            db.rollback()
            raise HTTPException(status_code=400, detail="Email already registered as a Teacher.")
            
        # Build dependent row targeting user_id back reference
        new_teacher_profile = Teacher(
            name=user_data.name,
            email=user_data.email,
            phone=user_data.phone,
            user_id=new_user.id
        )
        db.add(new_teacher_profile)
        
    # Commit changes safely to both tables atomically
    db.commit()
    db.refresh(new_user)
    
    return {"message": "Registration successful!", "user_id": new_user.id, "role": target_role.role}











@router.post("/refresh")
def refresh_access_token(body: TokenRefreshRequest, db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate refresh token",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        # Decode the token payload
        payload = jwt.decode(body.refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        token_type: str = payload.get("type")
        
        # Security Guard: Ensure they didn't pass an access token to the refresh endpoint!
        if username is None or token_type != "refresh":
            raise credentials_exception
            
    except JWTError:
        raise credentials_exception
        
    # Check if the user still exists in the system
    user = get_user(db, username=username)
    if user is None:
        raise credentials_exception
        
    # Issue a brand new access token
    new_access_token = create_access_token(data={"sub": user.username})
    
    return {
        "access_token": new_access_token,
        "token_type": "bearer"
    }