from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes: True
        
class UserRegisterRequest(BaseModel):
    username: str     # Used for system login credentials
    name: str         # The display name
    email: EmailStr   # Shared contact point
    phone: str        # Required dynamically if they register as a teacher
    password: str     
    role_id: int