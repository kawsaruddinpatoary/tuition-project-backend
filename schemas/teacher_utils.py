from pydantic import BaseModel


# Teaching Type
class TeachingTypeCreate(BaseModel):
    teaching_type: str

class TeachingTypeResponse(TeachingTypeCreate):
    id: int
    teaching_type: str

    class Config:
        orm_mode = True
        
# Admission Type
class AdmissionTypeCreate(BaseModel):
    admission_type: str

class AdmissionTypeResponse(AdmissionTypeCreate):
    id: int
    admission_type: str

    class Config:
        orm_mode = True

# Teaching Type Preference
class TeachingTypePreference(BaseModel):
    teacher_id: int
    teaching_type: int

# Admission Type Preference
class AdmissionPreference(BaseModel):
    teacher_id: int
    admission_type: int

# Preferred Area
class PreferredArea(BaseModel):
    teacher_id: int
    area: int

# Preferences
class PreferenceCreate(BaseModel):
    teacher_id: int
    min_salary: float
    max_salary: float
    group: int
    medium: int
    curriculum: int
    class_: int
    
class PreferenceResponse(PreferenceCreate):
    id: int
    teacher_id: int
    min_salary: float
    max_salary: float
    group: int
    medium: int
    curriculum: int
    class_: int

    class Config:
        orm_mode = True


# Preferred Subject
class PreferredSubject(BaseModel):
    subject: int
    preference_id: int

# Preferred Tuition Type
class PreferredTuitionType(BaseModel):
    tuition_type: int
    preference_id: int

# Preferred Time Slot
class PreferredTimeSlot(BaseModel):
    time_slot: int
    preference_id: int

