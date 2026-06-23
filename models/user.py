from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(50), unique=True)
    hashed_password = Column(String(100))
    is_active = Column(Boolean, default=True) 
    
    
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=False)
    role = relationship("Roles")
    
    
    teacher_profile = relationship("Teacher", back_populates="user", uselist=False)