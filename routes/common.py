from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from auth.dependencies import get_current_user
from db import get_db
from models.common import (Areas, EducationLevels, Boards, Groups, InstituteTypes, Mediums, Curriculums, Relationships, Roles, Subjects,
                           Departments, Genders, Religions, BloodGroups, TuitionTypes, TimeSlots, Classes, Addresses)
from models.teacher_utils import AdmissionTypes, TeachingTypes
from schemas.common import (AreaCreate, AreaResponse, EducationLevelCreate, EducationLevelResponse,
                            BoardCreate, BoardResponse, GroupCreate, GroupResponse, InstituteTypeCreate, InstituteTypeCreate, InstituteTypeResponse, MediumCreate, MediumResponse,
                            CurriculumCreate, CurriculumResponse, RelationshipCreate, RelationshipResponse, RoleCreate, RoleResponse, SubjectCreate, SubjectResponse,
                            DepartmentCreate, DepartmentResponse, GenderCreate, GenderResponse,
                            ReligionCreate, ReligionResponse, BloodGroupCreate, BloodGroupResponse,
                            TuitionTypeCreate, TuitionTypeResponse, AdmissionTypeCreate, AdmissionTypeResponse,
                            TeachingTypeCreate, TeachingTypeResponse, TimeSlotCreate, TimeSlotResponse,
                            ClassCreate, ClassResponse, AddressCreate, AddressResponse)
from typing import List

router = APIRouter(prefix="/commons", tags=["Commons"], dependencies=[Depends(get_current_user)])

# ==================== AREAS ====================
@router.get("/areas", response_model=List[AreaResponse])
def get_areas(db: Session = Depends(get_db)):
    areas = db.query(Areas).all()
    return areas

@router.get("/areas/{area_id}", response_model=AreaResponse)
def get_area(area_id: int, db: Session = Depends(get_db)):
    area = db.query(Areas).filter(Areas.id == area_id).first()
    if not area:
        raise HTTPException(status_code=404, detail="Area not found")
    return area

@router.post("/areas", response_model=AreaResponse, status_code=201)
def create_area(payload: AreaCreate, db: Session = Depends(get_db)):
    area = Areas(**payload.dict())
    db.add(area)
    db.commit()
    return area

@router.delete("/areas/{area_id}", status_code=204)
def delete_area(area_id: int, db: Session = Depends(get_db)):
    area = db.query(Areas).filter(Areas.id == area_id).first()
    if not area:
        raise HTTPException(status_code=404, detail="Area not found")
    db.delete(area)
    db.commit()

# ==================== EDUCATION LEVELS ====================
@router.get("/education-levels", response_model=List[EducationLevelResponse])
def get_education_levels(db: Session = Depends(get_db)):
    levels = db.query(EducationLevels).all()
    return levels

@router.get("/education-levels/{level_id}", response_model=EducationLevelResponse)
def get_education_level(level_id: int, db: Session = Depends(get_db)):
    level = db.query(EducationLevels).filter(EducationLevels.id == level_id).first()
    if not level:
        raise HTTPException(status_code=404, detail="Education level not found")
    return level

@router.post("/education-levels", response_model=EducationLevelResponse, status_code=201)
def create_education_level(payload: EducationLevelCreate, db: Session = Depends(get_db)):
    level = EducationLevels(**payload.dict())
    db.add(level)
    db.commit()
    return level

@router.delete("/education-levels/{level_id}", status_code=204)
def delete_education_level(level_id: int, db: Session = Depends(get_db)):
    level = db.query(EducationLevels).filter(EducationLevels.id == level_id).first()
    if not level:
        raise HTTPException(status_code=404, detail="Education level not found")
    db.delete(level)
    db.commit()

# ==================== BOARDS ====================
@router.get("/boards", response_model=List[BoardResponse])
def get_boards(db: Session = Depends(get_db)):
    boards = db.query(Boards).all()
    return boards

@router.get("/boards/{board_id}", response_model=BoardResponse)
def get_board(board_id: int, db: Session = Depends(get_db)):
    board = db.query(Boards).filter(Boards.id == board_id).first()
    if not board:
        raise HTTPException(status_code=404, detail="Board not found")
    return board

@router.post("/boards", response_model=BoardResponse, status_code=201)
def create_board(payload: BoardCreate, db: Session = Depends(get_db)):
    board = Boards(**payload.dict())
    db.add(board)
    db.commit()
    return board

@router.delete("/boards/{board_id}", status_code=204)
def delete_board(board_id: int, db: Session = Depends(get_db)):
    board = db.query(Boards).filter(Boards.id == board_id).first()
    if not board:
        raise HTTPException(status_code=404, detail="Board not found")
    db.delete(board)
    db.commit()

# ==================== GROUPS ====================
@router.get("/groups", response_model=List[GroupResponse])
def get_groups(db: Session = Depends(get_db)):
    groups = db.query(Groups).all()
    return groups

@router.get("/groups/{group_id}", response_model=GroupResponse)
def get_group(group_id: int, db: Session = Depends(get_db)):
    group = db.query(Groups).filter(Groups.id == group_id).first()
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    return group

@router.post("/groups", response_model=GroupResponse, status_code=201)
def create_group(payload: GroupCreate, db: Session = Depends(get_db)):
    group = Groups(**payload.dict())
    db.add(group)
    db.commit()
    return group

@router.delete("/groups/{group_id}", status_code=204)
def delete_group(group_id: int, db: Session = Depends(get_db)):
    group = db.query(Groups).filter(Groups.id == group_id).first()
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    db.delete(group)
    db.commit()

# ==================== MEDIUMS ====================
@router.get("/mediums", response_model=List[MediumResponse])
def get_mediums(db: Session = Depends(get_db)):
    mediums = db.query(Mediums).all()
    return mediums

@router.get("/mediums/{medium_id}", response_model=MediumResponse)
def get_medium(medium_id: int, db: Session = Depends(get_db)):
    medium = db.query(Mediums).filter(Mediums.id == medium_id).first()
    if not medium:
        raise HTTPException(status_code=404, detail="Medium not found")
    return medium

@router.post("/mediums", response_model=MediumResponse, status_code=201)
def create_medium(payload: MediumCreate, db: Session = Depends(get_db)):
    medium = Mediums(**payload.dict())
    db.add(medium)
    db.commit()
    return medium

@router.delete("/mediums/{medium_id}", status_code=204)
def delete_medium(medium_id: int, db: Session = Depends(get_db)):
    medium = db.query(Mediums).filter(Mediums.id == medium_id).first()
    if not medium:
        raise HTTPException(status_code=404, detail="Medium not found")
    db.delete(medium)
    db.commit()

# ==================== CURRICULUMS ====================
@router.get("/curriculums", response_model=List[CurriculumResponse])
def get_curriculums(db: Session = Depends(get_db)):
    curriculums = db.query(Curriculums).all()
    return curriculums

@router.get("/curriculums/{curriculum_id}", response_model=CurriculumResponse)
def get_curriculum(curriculum_id: int, db: Session = Depends(get_db)):
    curriculum = db.query(Curriculums).filter(Curriculums.id == curriculum_id).first()
    if not curriculum:
        raise HTTPException(status_code=404, detail="Curriculum not found")
    return curriculum

@router.post("/curriculums", response_model=CurriculumResponse, status_code=201)
def create_curriculum(payload: CurriculumCreate, db: Session = Depends(get_db)):
    curriculum = Curriculums(**payload.dict())
    db.add(curriculum)
    db.commit()
    return curriculum

@router.delete("/curriculums/{curriculum_id}", status_code=204)
def delete_curriculum(curriculum_id: int, db: Session = Depends(get_db)):
    curriculum = db.query(Curriculums).filter(Curriculums.id == curriculum_id).first()
    if not curriculum:
        raise HTTPException(status_code=404, detail="Curriculum not found")
    db.delete(curriculum)
    db.commit()

# ==================== SUBJECTS ====================
@router.get("/subjects", response_model=List[SubjectResponse])
def get_subjects(db: Session = Depends(get_db)):
    subjects = db.query(Subjects).all()
    return subjects

@router.get("/subjects/{subject_id}", response_model=SubjectResponse)
def get_subject(subject_id: int, db: Session = Depends(get_db)):
    subject = db.query(Subjects).filter(Subjects.id == subject_id).first()
    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    return subject

@router.post("/subjects", response_model=SubjectResponse, status_code=201)
def create_subject(payload: SubjectCreate, db: Session = Depends(get_db)):
    subject = Subjects(**payload.dict())
    db.add(subject)
    db.commit()
    return subject

@router.delete("/subjects/{subject_id}", status_code=204)
def delete_subject(subject_id: int, db: Session = Depends(get_db)):
    subject = db.query(Subjects).filter(Subjects.id == subject_id).first()
    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    db.delete(subject)
    db.commit()

# ==================== DEPARTMENTS ====================
@router.get("/departments", response_model=List[DepartmentResponse])
def get_departments(db: Session = Depends(get_db)):
    departments = db.query(Departments).all()
    return departments

@router.get("/departments/{department_id}", response_model=DepartmentResponse)
def get_department(department_id: int, db: Session = Depends(get_db)):
    department = db.query(Departments).filter(Departments.id == department_id).first()
    if not department:
        raise HTTPException(status_code=404, detail="Department not found")
    return department

@router.post("/departments", response_model=DepartmentResponse, status_code=201)
def create_department(payload: DepartmentCreate, db: Session = Depends(get_db)):
    department = Departments(**payload.dict())
    db.add(department)
    db.commit()
    return department

@router.delete("/departments/{department_id}", status_code=204)
def delete_department(department_id: int, db: Session = Depends(get_db)):
    department = db.query(Departments).filter(Departments.id == department_id).first()
    if not department:
        raise HTTPException(status_code=404, detail="Department not found")
    db.delete(department)
    db.commit()

# ==================== GENDERS ====================
@router.get("/genders", response_model=List[GenderResponse])
def get_genders(db: Session = Depends(get_db)):
    genders = db.query(Genders).all()
    return genders

@router.get("/genders/{gender_id}", response_model=GenderResponse)
def get_gender(gender_id: int, db: Session = Depends(get_db)):
    gender = db.query(Genders).filter(Genders.id == gender_id).first()
    if not gender:
        raise HTTPException(status_code=404, detail="Gender not found")
    return gender

@router.post("/genders", response_model=GenderResponse, status_code=201)
def create_gender(payload: GenderCreate, db: Session = Depends(get_db)):
    gender = Genders(**payload.dict())
    db.add(gender)
    db.commit()
    return gender

@router.delete("/genders/{gender_id}", status_code=204)
def delete_gender(gender_id: int, db: Session = Depends(get_db)):
    gender = db.query(Genders).filter(Genders.id == gender_id).first()
    if not gender:
        raise HTTPException(status_code=404, detail="Gender not found")
    db.delete(gender)
    db.commit()

# ==================== RELIGIONS ====================
@router.get("/religions", response_model=List[ReligionResponse])
def get_religions(db: Session = Depends(get_db)):
    religions = db.query(Religions).all()
    return religions

@router.get("/religions/{religion_id}", response_model=ReligionResponse)
def get_religion(religion_id: int, db: Session = Depends(get_db)):
    religion = db.query(Religions).filter(Religions.id == religion_id).first()
    if not religion:
        raise HTTPException(status_code=404, detail="Religion not found")
    return religion

@router.post("/religions", response_model=ReligionResponse, status_code=201)
def create_religion(payload: ReligionCreate, db: Session = Depends(get_db)):
    religion = Religions(**payload.dict())
    db.add(religion)
    db.commit()
    return religion

@router.delete("/religions/{religion_id}", status_code=204)
def delete_religion(religion_id: int, db: Session = Depends(get_db)):
    religion = db.query(Religions).filter(Religions.id == religion_id).first()
    if not religion:
        raise HTTPException(status_code=404, detail="Religion not found")
    db.delete(religion)
    db.commit()

# ==================== BLOOD GROUPS ====================
@router.get("/blood-groups", response_model=List[BloodGroupResponse])
def get_blood_groups(db: Session = Depends(get_db)):
    groups = db.query(BloodGroups).all()
    return groups

@router.get("/blood-groups/{blood_group_id}", response_model=BloodGroupResponse)
def get_blood_group(blood_group_id: int, db: Session = Depends(get_db)):
    group = db.query(BloodGroups).filter(BloodGroups.id == blood_group_id).first()
    if not group:
        raise HTTPException(status_code=404, detail="Blood group not found")
    return group

@router.post("/blood-groups", response_model=BloodGroupResponse, status_code=201)
def create_blood_group(payload: BloodGroupCreate, db: Session = Depends(get_db)):
    group = BloodGroups(**payload.dict())
    db.add(group)
    db.commit()
    return group

@router.delete("/blood-groups/{blood_group_id}", status_code=204)
def delete_blood_group(blood_group_id: int, db: Session = Depends(get_db)):
    group = db.query(BloodGroups).filter(BloodGroups.id == blood_group_id).first()
    if not group:
        raise HTTPException(status_code=404, detail="Blood group not found")
    db.delete(group)
    db.commit()

# ==================== TUITION TYPES ====================
@router.get("/tuition-types", response_model=List[TuitionTypeResponse])
def get_tuition_types(db: Session = Depends(get_db)):
    types = db.query(TuitionTypes).all()
    return types

@router.get("/tuition-types/{tuition_type_id}", response_model=TuitionTypeResponse)
def get_tuition_type(tuition_type_id: int, db: Session = Depends(get_db)):
    ttype = db.query(TuitionTypes).filter(TuitionTypes.id == tuition_type_id).first()
    if not ttype:
        raise HTTPException(status_code=404, detail="Tuition type not found")
    return ttype

@router.post("/tuition-types", response_model=TuitionTypeResponse, status_code=201)
def create_tuition_type(payload: TuitionTypeCreate, db: Session = Depends(get_db)):
    ttype = TuitionTypes(**payload.dict())
    db.add(ttype)
    db.commit()
    return ttype

@router.delete("/tuition-types/{tuition_type_id}", status_code=204)
def delete_tuition_type(tuition_type_id: int, db: Session = Depends(get_db)):
    ttype = db.query(TuitionTypes).filter(TuitionTypes.id == tuition_type_id).first()
    if not ttype:
        raise HTTPException(status_code=404, detail="Tuition type not found")
    db.delete(ttype)
    db.commit()

# ==================== ADMISSION TYPES ====================
@router.get("/admission-types", response_model=List[AdmissionTypeResponse])
def get_admission_types(db: Session = Depends(get_db)):
    types = db.query(AdmissionTypes).all()
    return types

@router.get("/admission-types/{admission_type_id}", response_model=AdmissionTypeResponse)
def get_admission_type(admission_type_id: int, db: Session = Depends(get_db)):
    atype = db.query(AdmissionTypes).filter(AdmissionTypes.id == admission_type_id).first()
    if not atype:
        raise HTTPException(status_code=404, detail="Admission type not found")
    return atype

@router.post("/admission-types", response_model=AdmissionTypeResponse, status_code=201)
def create_admission_type(payload: AdmissionTypeCreate, db: Session = Depends(get_db)):
    atype = AdmissionTypes(**payload.dict())
    db.add(atype)
    db.commit()
    return atype

@router.delete("/admission-types/{admission_type_id}", status_code=204)
def delete_admission_type(admission_type_id: int, db: Session = Depends(get_db)):
    atype = db.query(AdmissionTypes).filter(AdmissionTypes.id == admission_type_id).first()
    if not atype:
        raise HTTPException(status_code=404, detail="Admission type not found")
    db.delete(atype)
    db.commit()

# ==================== TEACHING TYPES ====================
@router.get("/teaching-types", response_model=List[TeachingTypeResponse])
def get_teaching_types(db: Session = Depends(get_db)):
    types = db.query(TeachingTypes).all()
    return types

@router.get("/teaching-types/{teaching_type_id}", response_model=TeachingTypeResponse)
def get_teaching_type(teaching_type_id: int, db: Session = Depends(get_db)):
    ttype = db.query(TeachingTypes).filter(TeachingTypes.id == teaching_type_id).first()
    if not ttype:
        raise HTTPException(status_code=404, detail="Teaching type not found")
    return ttype

@router.post("/teaching-types", response_model=TeachingTypeResponse, status_code=201)
def create_teaching_type(payload: TeachingTypeCreate, db: Session = Depends(get_db)):
    ttype = TeachingTypes(**payload.dict())
    db.add(ttype)
    db.commit()
    return ttype

@router.delete("/teaching-types/{teaching_type_id}", status_code=204)
def delete_teaching_type(teaching_type_id: int, db: Session = Depends(get_db)):
    ttype = db.query(TeachingTypes).filter(TeachingTypes.id == teaching_type_id).first()
    if not ttype:
        raise HTTPException(status_code=404, detail="Teaching type not found")
    db.delete(ttype)
    db.commit()

# ==================== TIME SLOTS ====================
@router.get("/time-slots", response_model=List[TimeSlotResponse])
def get_time_slots(db: Session = Depends(get_db)):
    slots = db.query(TimeSlots).all()
    return slots

@router.get("/time-slots/{time_slot_id}", response_model=TimeSlotResponse)
def get_time_slot(time_slot_id: int, db: Session = Depends(get_db)):
    slot = db.query(TimeSlots).filter(TimeSlots.id == time_slot_id).first()
    if not slot:
        raise HTTPException(status_code=404, detail="Time slot not found")
    return slot

@router.post("/time-slots", response_model=TimeSlotResponse, status_code=201)
def create_time_slot(payload: TimeSlotCreate, db: Session = Depends(get_db)):
    slot = TimeSlots(**payload.dict())
    db.add(slot)
    db.commit()
    return slot

@router.delete("/time-slots/{time_slot_id}", status_code=204)
def delete_time_slot(time_slot_id: int, db: Session = Depends(get_db)):
    slot = db.query(TimeSlots).filter(TimeSlots.id == time_slot_id).first()
    if not slot:
        raise HTTPException(status_code=404, detail="Time slot not found")
    db.delete(slot)
    db.commit()

# ==================== CLASSES ====================
@router.get("/classes", response_model=List[ClassResponse])
def get_classes(db: Session = Depends(get_db)):
    classes = db.query(Classes).all()
    return classes

@router.get("/classes/{class_id}", response_model=ClassResponse)
def get_class(class_id: int, db: Session = Depends(get_db)):
    cls = db.query(Classes).filter(Classes.id == class_id).first()
    if not cls:
        raise HTTPException(status_code=404, detail="Class not found")
    return cls

@router.post("/classes", response_model=ClassResponse, status_code=201)
def create_class(payload: ClassCreate, db: Session = Depends(get_db)):
    cls = Classes(**payload.dict())
    db.add(cls)
    db.commit()
    return cls

@router.delete("/classes/{class_id}", status_code=204)
def delete_class(class_id: int, db: Session = Depends(get_db)):
    cls = db.query(Classes).filter(Classes.id == class_id).first()
    if not cls:
        raise HTTPException(status_code=404, detail="Class not found")
    db.delete(cls)
    db.commit()

# ==================== ADDRESSES ====================
@router.get("/addresses", response_model=List[AddressResponse])
def get_addresses(db: Session = Depends(get_db)):
    addresses = db.query(Addresses).all()
    return addresses

@router.get("/addresses/{address_id}", response_model=AddressResponse)
def get_address(address_id: int, db: Session = Depends(get_db)):
    address = db.query(Addresses).filter(Addresses.id == address_id).first()
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    return address

@router.post("/addresses", response_model=AddressResponse, status_code=201)
def create_address(payload: AddressCreate, db: Session = Depends(get_db)):
    address = Addresses(**payload.dict())
    db.add(address)
    db.commit()
    return address

@router.delete("/addresses/{address_id}", status_code=204)
def delete_address(address_id: int, db: Session = Depends(get_db)):
    address = db.query(Addresses).filter(Addresses.id == address_id).first()
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    db.delete(address)
    db.commit()
    
@router.get('/roles', response_model=List[RoleResponse])
def get_all_roles(db: Session = Depends(get_db)):
    roles = db.query(Roles).all()
    return roles

@router.get("/roles/{role_id}", response_model=RoleResponse)
def get_roles(role_id: int, db: Session = Depends(get_db)):
    role = db.query(Roles).filter(Roles.id == role_id).first()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role

@router.post("/roles", response_model=RoleResponse, status_code=201)
def create_roles(payload: RoleCreate, db: Session = Depends(get_db)):
    role = Roles(**payload.dict())
    db.add(role)
    db.commit()
    return role

@router.delete("/roles/{role_id}", status_code=204)
def delete_role(role_id: int, db: Session = Depends(get_db)):
    role = db.query(Roles).filter(Roles.id == role_id).first()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    db.delete(role)
    db.commit()

  
@router.get("/institute-types", response_model=List[InstituteTypeResponse])
def get_institute_types(db: Session = Depends(get_db)):
    itypes = db.query(InstituteTypes).all()
    return itypes

@router.get("/institute-types/{institute_type_id}", response_model=InstituteTypeResponse)
def get_institute_type(institute_type_id: int, db: Session = Depends(get_db)):
    itype = db.query(InstituteTypes).filter(InstituteTypes.id == institute_type_id).first()
    if not itype:
        raise HTTPException(status_code=404, detail="Institute type not found")
    return itype

@router.post("/institute-types", response_model=InstituteTypeResponse, status_code=201)
def create_institute_type(payload: InstituteTypeCreate, db: Session = Depends(get_db)):
    itype = InstituteTypes(**payload.dict())
    db.add(itype)
    db.commit()
    return itype

@router.delete("/institute-types/{institute_type_id}", status_code=204)
def delete_institute_type(institute_type_id: int, db: Session = Depends(get_db)):
    itype = db.query(InstituteTypes).filter(InstituteTypes.id == institute_type_id).first()
    if not itype:
        raise HTTPException(status_code=404, detail="Institute type not found")
    db.delete(itype)
    db.commit()

@router.get("/relationships", response_model=List[RelationshipResponse])
def get_relationships(db: Session = Depends(get_db)):
    relationships = db.query(Relationships).all()
    return relationships

@router.get("/relationships/{relationship_id}", response_model=RelationshipResponse)
def get_relationship(relationship_id: int, db: Session = Depends(get_db)):
    relationship = db.query(Relationships).filter(Relationships.id == relationship_id).first()
    if not relationship:
        raise HTTPException(status_code=404, detail="Relationship not found")
    return relationship

@router.post("/relationships", response_model=RelationshipResponse, status_code=201)
def create_relationship(payload: RelationshipCreate, db: Session = Depends(get_db)):
    relationship = Relationships(**payload.dict())
    db.add(relationship)
    db.commit()
    return relationship

@router.delete("/relationships/{relationship_id}", status_code=204)
def delete_relationship(relationship_id: int, db: Session = Depends(get_db)):
    relationship = db.query(Relationships).filter(Relationships.id == relationship_id).first()
    if not relationship:
        raise HTTPException(status_code=404, detail="Relationship not found")
    db.delete(relationship)
    db.commit()