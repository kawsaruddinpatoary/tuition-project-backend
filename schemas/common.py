from pydantic import BaseModel

# Area
class AreaCreate(BaseModel):
    area: str
    
class AreaResponse(AreaCreate):
    id: int
    area: str

    class Config:
        orm_mode = True

# Education Level
class EducationLevelCreate(BaseModel):
    level: str
    
class EducationLevelResponse(EducationLevelCreate):
    id: int
    level: str

    class Config:
        orm_mode = True
        
# Board
class BoardCreate(BaseModel):
    board: str
    
class BoardResponse(BoardCreate):
    id: int
    board: str

    class Config:
        orm_mode = True

# Group
class GroupCreate(BaseModel):
    group: str

class GroupResponse(GroupCreate):
    id: int
    group: str

    class Config:
        orm_mode = True

# Medium
class MediumCreate(BaseModel):
    medium: str
    
class MediumResponse(MediumCreate):
    id: int
    medium: str

    class Config:
        orm_mode = True

# Curriculum
class CurriculumCreate(BaseModel):
    curriculum: str

class CurriculumResponse(CurriculumCreate):
    id: int
    curriculum: str

    class Config:
        orm_mode = True

# Subject
class SubjectCreate(BaseModel):
    subject: str

class SubjectResponse(SubjectCreate):
    id: int
    subject: str

    class Config:
        orm_mode = True

# Department
class DepartmentCreate(BaseModel):
    department: str
    
class DepartmentResponse(DepartmentCreate):
    id: int
    department: str

    class Config:
        orm_mode = True

# Gender
class GenderCreate(BaseModel):
    gender: str

class GenderResponse(GenderCreate):
    id: int
    gender: str

    class Config:
        orm_mode = True

# Religion
class ReligionCreate(BaseModel):
    religion: str

class ReligionResponse(ReligionCreate):
    id: int
    religion: str

    class Config:
        orm_mode = True

# Blood Group
class BloodGroupCreate(BaseModel):
    blood_group: str

class BloodGroupResponse(BloodGroupCreate):
    id: int
    blood_group: str

    class Config:
        orm_mode = True

# Time Slot
class TimeSlotCreate(BaseModel):
    time_slot: str

class TimeSlotResponse(TimeSlotCreate):
    id: int
    time_slot: str

    class Config:
        orm_mode = True

# Tuition Type
class TuitionTypeCreate(BaseModel):
    tuition_type: str

class TuitionTypeResponse(TuitionTypeCreate):
    id: int
    tuition_type: str

    class Config:
        orm_mode = True

# classes
class ClassCreate(BaseModel):
    class_: str

class ClassResponse(ClassCreate):
    id: int
    class_: str

    class Config:
        orm_mode = True
        
# addresses
class AddressCreate(BaseModel):
    division: str
    city: str
    area: str
    road: str | None = None
    building: str | None = None
    full_address: str

class AddressResponse(AddressCreate):
    id: int
    division: str
    city: str
    area: str
    road: str | None = None
    building: str | None = None
    full_address: str

    class Config:
        orm_mode = True