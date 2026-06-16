from datetime import date
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from .teacher_utils import PreferenceResponse, TeachingTypePreference, AdmissionPreference, PreferredArea
from .teacher_utils import PreferredSubject, PreferredTuitionType, PreferredTimeSlot
from .common import AddressResponse

class TeacherCreate(BaseModel):
    name: str
    email: EmailStr

class TeacherResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True

# Personal Info - Input schema (no teacher_id, comes from URL)
class PersonalInfoCreate(BaseModel):
    father_name: str
    mother_name: str
    date_of_birth: date
    bio: Optional[str] = None
    gender: int
    religion: int
    blood_group: int
    present_address: int
    permanent_address: int

# Personal Info - Full schema with teacher_id
class PersonalInfo(PersonalInfoCreate):
    teacher_id: int

class PersonalInfoResponse(PersonalInfo):
    present_address_rel: Optional[AddressResponse] = None
    permanent_address_rel: Optional[AddressResponse] = None

# Teacher Info - Input schema (no teacher_id)
class TeacherInfoCreate(BaseModel):
    group: int
    medium: int
    curriculum: Optional[int] = None

# Teacher Info - Full schema with teacher_id
class TeacherInfo(TeacherInfoCreate):
    teacher_id: int

# Contacts - Input schema (no teacher_id)
class ContactsCreate(BaseModel):
    phone: str
    whatsapp_number: Optional[str] = None
    secondary_phone: Optional[str] = None

# Contacts - Full schema with teacher_id
class ContactInfo(ContactsCreate):
    teacher_id: int

# School - Input schema (no teacher_id)
class SchoolCreateInput(BaseModel):
    name: str
    passing_year: int
    grade: float
    board: int
    group: int
    medium: int
    curriculum: Optional[int] = None

# School - Full schema with teacher_id
class SchoolCreate(SchoolCreateInput):
    teacher_id: int

class SchoolResponse(SchoolCreate):
    id: int

    class Config:
        orm_mode = True

# College - Input schema (no teacher_id)
class CollegeCreateInput(BaseModel):
    name: str
    passing_year: int
    grade: float
    board: int
    group: int
    medium: int
    curriculum: Optional[int] = None

# College - Full schema with teacher_id
class CollegeCreate(CollegeCreateInput):
    teacher_id: int

class CollegeResponse(CollegeCreate):
    id: int

    class Config:
        orm_mode = True

# University - Input schema (no teacher_id)
class UniversityCreateInput(BaseModel):
    name: str
    passing_year: int
    enroll_year: int
    grade: float
    department: int
    level: int

# University - Full schema with teacher_id
class UniversityCreate(UniversityCreateInput):
    teacher_id: int

class UniversityResponse(UniversityCreate):
    id: int

    class Config:
        orm_mode = True

# Full aggregated teacher response including all related data
class TeacherFullResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    personal: Optional[PersonalInfoResponse] = None
    info: Optional[TeacherInfo] = None
    contacts: Optional[ContactInfo] = None
    schools: List[SchoolResponse] = []
    colleges: List[CollegeResponse] = []
    universities: List[UniversityResponse] = []
    preferences: List[PreferenceResponse] = []
    teaching_type_preferences: List[TeachingTypePreference] = []
    admission_preferences: List[AdmissionPreference] = []
    preferred_areas: List[PreferredArea] = []

    class Config:
        orm_mode = True
