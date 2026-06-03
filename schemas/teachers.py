from pydantic import BaseModel, EmailStr

class TeacherCreate(BaseModel):
    name: str
    email: EmailStr

class TeacherResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True

class PersonalInfo(BaseModel):
    teacher_id: int
    father_name: str
    mother_name: str
    date_of_birth: str  # Use string format for date input
    bio: str | None = None
    gender: int
    religion: int
    blood_group: int
    present_address: int
    permanent_address: int

class TeacherInfo(BaseModel):
    teacher_id: int
    group: int
    medium: int
    curriculum: int

class ContactInfo(BaseModel):
    teacher_id: int
    phone: str
    whatsapp_number: str | None = None
    secondary_phone: str | None = None

class SchoolCreate(BaseModel):
    teacher_id: int
    name: str
    passing_year: int
    grade: float
    board: int
    group: int
    medium: int
    curriculum: int

class SchoolResponse(SchoolCreate):
    id: int
    teacher_id: int
    name: str
    passing_year: int
    grade: float
    board: int
    group: int
    medium: int
    curriculum: int

    class Config:
        orm_mode = True
        
        
class CollegeCreate(BaseModel):
    teacher_id: int
    name: str
    passing_year: int
    grade: float
    board: int
    group: int
    medium: int
    curriculum: int

class CollegeResponse(CollegeCreate):
    id: int
    teacher_id: int
    name: str
    passing_year: int
    grade: float
    board: int
    group: int
    medium: int
    curriculum: int

    class Config:
        orm_mode = True
        
        
class UniversityCreate(BaseModel):
    teacher_id: int
    name: str
    passing_year: int
    enroll_year: int
    grade: float
    department: int
    level: int

class UniversityResponse(UniversityCreate):
    id: int
    teacher_id: int
    name: str
    passing_year: int
    enroll_year: int
    grade: float
    department: int
    level: int

    class Config:
        orm_mode = True