from __future__ import annotations
from typing import List, Optional
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

# Teaching Type Preference - Input (no teacher_id)
class TeachingTypePreferenceInput(BaseModel):
    teaching_type: int

# Teaching Type Preference - Full with teacher_id
class TeachingTypePreference(TeachingTypePreferenceInput):
    teacher_id: int

# Admission Type Preference - Input (no teacher_id)
class AdmissionPreferenceInput(BaseModel):
    admission_type: int

# Admission Type Preference - Full with teacher_id
class AdmissionPreference(AdmissionPreferenceInput):
    teacher_id: int

# Preferred Area - Input (no teacher_id)
class PreferredAreaInput(BaseModel):
    area: int

# Preferred Area - Full with teacher_id
class PreferredArea(PreferredAreaInput):
    teacher_id: int

# Preferences - Input (no teacher_id)
class PreferenceCreateInput(BaseModel):
    min_salary: float
    max_salary: float
    group: int
    medium: int
    curriculum: int
    class_: int
    
# Preferences - Full with teacher_id
class PreferenceCreate(PreferenceCreateInput):
    teacher_id: int
    
class PreferenceResponse(PreferenceCreate):
    id: int
    teacher_id: int
    min_salary: float
    max_salary: float
    group: int
    medium: int
    curriculum: int
    class_: int
    preferred_subjects: List[PreferredSubject] = []
    preferred_tuition_types: List[PreferredTuitionType] = []
    preferred_time_slots: List[PreferredTimeSlot] = []

    class Config:
        orm_mode = True


# Preferred Subject - Input (no preference_id)
class PreferredSubjectInput(BaseModel):
    subject: int

# Preferred Subject - Full with preference_id
class PreferredSubject(PreferredSubjectInput):
    preference_id: int

# Preferred Tuition Type - Input (no preference_id)
class PreferredTuitionTypeInput(BaseModel):
    tuition_type: int

# Preferred Tuition Type - Full with preference_id
class PreferredTuitionType(PreferredTuitionTypeInput):
    preference_id: int

# Preferred Time Slot - Input (no preference_id)
class PreferredTimeSlotInput(BaseModel):
    time_slot: int

# Preferred Time Slot - Full with preference_id
class PreferredTimeSlot(PreferredTimeSlotInput):
    preference_id: int

