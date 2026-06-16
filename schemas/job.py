from datetime import date 
from pydantic import BaseModel, EmailStr
from typing import List, Optional

class JobCreate(BaseModel):
    creator: str
    email: EmailStr
    phone: str
    relation_with_student: int
    description: str
    start_date: date
    is_nagotiable: bool
    is_urgent: bool

class JobCreateResponse(JobCreate):
    id: int

    class Config:
        orm_mode = True

class JobInfoCreate(BaseModel):
    min_salary: int
    max_salary: int
    no_of_students: int
    days: int
    hours: int
    address: int
    institute_type: int
    
class JobInfoCreateResponse(JobInfoCreate):
    job_id : int
    
    class Config:
        orm_mode = True,
        from_attributes  = True 

class JobPreferencesCreate(BaseModel):
    group: int
    medium: int
    curriculum: int  
    gender: int
    time: int
    tuition_type: int
    area: int  

class JobPreferencesCreateResponse(JobPreferencesCreate):
    id: int

    class Config:
        orm_mode = True


class SubjectJobPreferenceCreate(BaseModel):
    subject: int

class SubjectJobPreferences(SubjectJobPreferenceCreate):
    id: int 
    preference_id: int
    
    class Config:
        orm_mode = True

class JobPreferencesResponse(JobPreferencesCreateResponse):
    subjects: List[SubjectJobPreferences] = []

    class Config:
        orm_mode = True  


class JobResponse(JobCreateResponse):
    job_info: Optional[JobInfoCreateResponse] = None
    preferences: Optional[JobPreferencesResponse] = None
    
    class Config:
        orm_model = True
        from_attributes = True