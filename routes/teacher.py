from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, selectinload
from sqlalchemy.exc import IntegrityError
from db import get_db
from models.teachers import Teacher, PersonalInfo, TeacherInfo, Contacts, Schools, Colleges, Universities
from models.teacher_utils import Preferences, PreferredSubjects, PreferredTuitionTypes, PreferredTimeSlots
from models.teacher_utils import TeachingTypePreferences, AdmissionPreferences, PreferredAreas
from schemas.teachers import (PersonalInfoCreate, TeacherInfoCreate, ContactsCreate, 
                              SchoolCreateInput, SchoolResponse, CollegeCreateInput, CollegeResponse, 
                              UniversityCreateInput, UniversityResponse)
from schemas.teacher_utils import (PreferenceCreateInput, PreferenceResponse, 
                                   TeachingTypePreferenceInput, AdmissionPreferenceInput, PreferredAreaInput,
                                   PreferredSubjectInput, PreferredTuitionTypeInput, PreferredTimeSlotInput)

router = APIRouter()


def serialize_address(address):
    if not address:
        return None
    return {
        "id": address.id,
        "division": address.division,
        "city": address.city,
        "area": address.area,
        "road": address.road,
        "building": address.building,
        "full_address": address.full_address,
    }


def serialize_personal_info(personal):
    if not personal:
        return None
    return {
        "teacher_id": personal.teacher_id,
        "father_name": personal.father_name,
        "mother_name": personal.mother_name,
        "date_of_birth": personal.date_of_birth,
        "bio": personal.bio,
        "gender": personal.gender_rel.gender if getattr(personal, "gender_rel", None) else None,
        "religion": personal.religion_rel.religion if getattr(personal, "religion_rel", None) else None,
        "blood_group": personal.blood_group_rel.blood_group if getattr(personal, "blood_group_rel", None) else None,
        "present_address": serialize_address(getattr(personal, "present_address_rel", None)),
        "permanent_address": serialize_address(getattr(personal, "permanent_address_rel", None)),
    }


def serialize_teacher_info(info):
    if not info:
        return None
    return {
        "teacher_id": info.teacher_id,
        "group": info.group_rel.group if getattr(info, "group_rel", None) else None,
        "medium": info.medium_rel.medium if getattr(info, "medium_rel", None) else None,
        "curriculum": info.curriculum_rel.curriculum if getattr(info, "curriculum_rel", None) else None,
    }


def serialize_school_record(record):
    return {
        "id": record.id,
        "teacher_id": record.teacher_id,
        "name": record.name,
        "passing_year": record.passing_year,
        "grade": record.grade,
        "board": record.board_rel.board if getattr(record, "board_rel", None) else None,
        "group": record.group_rel.group if getattr(record, "group_rel", None) else None,
        "medium": record.medium_rel.medium if getattr(record, "medium_rel", None) else None,
        "curriculum": record.curriculum_rel.curriculum if getattr(record, "curriculum_rel", None) else None,
    }


def serialize_university(record):
    return {
        "id": record.id,
        "teacher_id": record.teacher_id,
        "name": record.name,
        "passing_year": record.passing_year,
        "enroll_year": record.enroll_year,
        "grade": record.grade,
        "department": record.department_rel.department if getattr(record, "department_rel", None) else None,
        "level": record.level_rel.level if getattr(record, "level_rel", None) else None,
    }


def serialize_preference(pref):
    return {
        "id": pref.id,
        "teacher_id": pref.teacher_id,
        "min_salary": pref.min_salary,
        "max_salary": pref.max_salary,
        "group": pref.group_rel.group if getattr(pref, "group_rel", None) else None,
        "medium": pref.medium_rel.medium if getattr(pref, "medium_rel", None) else None,
        "curriculum": pref.curriculum_rel.curriculum if getattr(pref, "curriculum_rel", None) else None,
        "class_": pref.class_rel.class_name if getattr(pref, "class_rel", None) else None,
        "preferred_subjects": [
            subject.subject_rel.subject if getattr(subject, "subject_rel", None) else None
            for subject in pref.preferred_subjects
        ],
        "preferred_tuition_types": [
            tt.tuition_type_rel.tuition_type if getattr(tt, "tuition_type_rel", None) else None
            for tt in pref.preferred_tuition_types
        ],
        "preferred_time_slots": [
            ts.time_slot_rel.time_slot if getattr(ts, "time_slot_rel", None) else None
            for ts in pref.preferred_time_slots
        ],
    }


def serialize_teaching_type_preference(pref):
    return {
        "teacher_id": pref.teacher_id,
        "teaching_type": pref.teaching_type_rel.teaching_type if getattr(pref, "teaching_type_rel", None) else None,
    }


def serialize_admission_preference(pref):
    return {
        "teacher_id": pref.teacher_id,
        "admission_type": pref.admission_type_rel.admission_type if getattr(pref, "admission_type_rel", None) else None,
    }


def serialize_preferred_area(pref):
    return {
        "teacher_id": pref.teacher_id,
        "area": pref.area_rel.area if getattr(pref, "area_rel", None) else None,
    }


def serialize_teacher(teacher):
    return {
        "id": teacher.id,
        "name": teacher.name,
        "email": teacher.email,
        "personal": serialize_personal_info(teacher.personal),
        "info": serialize_teacher_info(teacher.info),
        "contacts": {
            "teacher_id": teacher.contacts.teacher_id,
            "phone": teacher.contacts.phone,
            "whatsapp_number": teacher.contacts.whatsapp_number,
            "secondary_phone": teacher.contacts.secondary_phone,
        } if teacher.contacts else None,
        "schools": [serialize_school_record(s) for s in teacher.schools],
        "colleges": [serialize_school_record(c) for c in teacher.colleges],
        "universities": [serialize_university(u) for u in teacher.universities],
        "preferences": [serialize_preference(p) for p in teacher.preferences],
        "teaching_type_preferences": [serialize_teaching_type_preference(p) for p in teacher.teaching_type_preferences],
        "admission_preferences": [serialize_admission_preference(p) for p in teacher.admission_preferences],
        "preferred_areas": [serialize_preferred_area(a) for a in teacher.preferred_areas],
    }


@router.get("/teachers")
def list_teachers(db: Session = Depends(get_db)):
    teachers = db.query(Teacher).options(
        selectinload(Teacher.personal),
        selectinload(Teacher.info),
        selectinload(Teacher.contacts),
        selectinload(Teacher.schools),
        selectinload(Teacher.colleges),
        selectinload(Teacher.universities),
        selectinload(Teacher.teaching_type_preferences),
        selectinload(Teacher.admission_preferences),
        selectinload(Teacher.preferred_areas),
        selectinload(Teacher.preferences).selectinload(Preferences.preferred_subjects),
        selectinload(Teacher.preferences).selectinload(Preferences.preferred_tuition_types),
        selectinload(Teacher.preferences).selectinload(Preferences.preferred_time_slots),
    ).all()
    return [serialize_teacher(teacher) for teacher in teachers]


@router.get("/teachers/{teacher_id}")
def get_teacher(teacher_id: int, db: Session = Depends(get_db)):
    teacher = db.query(Teacher).options(
        selectinload(Teacher.personal),
        selectinload(Teacher.info),
        selectinload(Teacher.contacts),
        selectinload(Teacher.schools),
        selectinload(Teacher.colleges),
        selectinload(Teacher.universities),
        selectinload(Teacher.teaching_type_preferences),
        selectinload(Teacher.admission_preferences),
        selectinload(Teacher.preferred_areas),
        selectinload(Teacher.preferences).selectinload(Preferences.preferred_subjects),
        selectinload(Teacher.preferences).selectinload(Preferences.preferred_tuition_types),
        selectinload(Teacher.preferences).selectinload(Preferences.preferred_time_slots),
    ).filter(Teacher.id == teacher_id).one_or_none()
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")

    return {
        "id": teacher.id,
        "name": teacher.name,
        "email": teacher.email,
        "personal": serialize_personal_info(teacher.personal),
        "info": serialize_teacher_info(teacher.info),
        "contacts": {
            "teacher_id": teacher.contacts.teacher_id,
            "phone": teacher.contacts.phone,
            "whatsapp_number": teacher.contacts.whatsapp_number,
            "secondary_phone": teacher.contacts.secondary_phone,
        } if teacher.contacts else None,
        "schools": [serialize_school_record(s) for s in teacher.schools],
        "colleges": [serialize_school_record(c) for c in teacher.colleges],
        "universities": [serialize_university(u) for u in teacher.universities],
        "preferences": [serialize_preference(p) for p in teacher.preferences],
        "teaching_type_preferences": [serialize_teaching_type_preference(p) for p in teacher.teaching_type_preferences],
        "admission_preferences": [serialize_admission_preference(p) for p in teacher.admission_preferences],
        "preferred_areas": [serialize_preferred_area(a) for a in teacher.preferred_areas],
    }

# Main teacher creation (name + email only)
@router.post("/teachers", status_code=201)
def create_teacher(name: str, email: str, db: Session = Depends(get_db)):
    try:
        t = Teacher(name=name, email=email)
        db.add(t)
        db.commit()
        return {"id": t.id, "name": t.name, "email": t.email}
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Email already exists")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

# Personal info endpoint
@router.post("/teachers/{teacher_id}/personal")
def add_personal_info(teacher_id: int, payload: PersonalInfoCreate, db: Session = Depends(get_db)):
    try:
        if not db.query(Teacher).filter(Teacher.id == teacher_id).first():
            raise HTTPException(status_code=404, detail="Teacher not found")
        
        # Check if personal info already exists
        existing = db.query(PersonalInfo).filter(PersonalInfo.teacher_id == teacher_id).first()
        if existing:
            raise HTTPException(status_code=409, detail="Personal info already exists for this teacher")
        
        personal = PersonalInfo(teacher_id=teacher_id, **payload.dict())
        db.add(personal)
        db.commit()
        return {"message": "Personal info added"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

# Teacher info endpoint
@router.post("/teachers/{teacher_id}/info")
def add_teacher_info(teacher_id: int, payload: TeacherInfoCreate, db: Session = Depends(get_db)):
    try:
        if not db.query(Teacher).filter(Teacher.id == teacher_id).first():
            raise HTTPException(status_code=404, detail="Teacher not found")
        
        # Check if teacher info already exists
        existing = db.query(TeacherInfo).filter(TeacherInfo.teacher_id == teacher_id).first()
        if existing:
            raise HTTPException(status_code=409, detail="Teacher info already exists for this teacher")
        
        info = TeacherInfo(teacher_id=teacher_id, **payload.dict())
        db.add(info)
        db.commit()
        return {"message": "Teacher info added"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

# Contacts endpoint
@router.post("/teachers/{teacher_id}/contacts")
def add_contacts(teacher_id: int, payload: ContactsCreate, db: Session = Depends(get_db)):
    try:
        if not db.query(Teacher).filter(Teacher.id == teacher_id).first():
            raise HTTPException(status_code=404, detail="Teacher not found")
        
        # Check if contacts already exist
        existing = db.query(Contacts).filter(Contacts.teacher_id == teacher_id).first()
        if existing:
            raise HTTPException(status_code=409, detail="Contacts already exist for this teacher")
        
        contacts = Contacts(teacher_id=teacher_id, **payload.dict())
        db.add(contacts)
        db.commit()
        return {"message": "Contacts added"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

# School endpoint
@router.post("/teachers/{teacher_id}/schools")
def add_school(teacher_id: int, payload: SchoolCreateInput, db: Session = Depends(get_db)):
    try:
        if not db.query(Teacher).filter(Teacher.id == teacher_id).first():
            raise HTTPException(status_code=404, detail="Teacher not found")
        
        school = Schools(teacher_id=teacher_id, **payload.dict())
        db.add(school)
        db.commit()
        return {"id": school.id, "message": "School record added"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

# College endpoint
@router.post("/teachers/{teacher_id}/colleges")
def add_college(teacher_id: int, payload: CollegeCreateInput, db: Session = Depends(get_db)):
    try:
        if not db.query(Teacher).filter(Teacher.id == teacher_id).first():
            raise HTTPException(status_code=404, detail="Teacher not found")
        
        college = Colleges(teacher_id=teacher_id, **payload.dict())
        db.add(college)
        db.commit()
        return {"id": college.id, "message": "College record added"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

# University endpoint
@router.post("/teachers/{teacher_id}/universities")
def add_university(teacher_id: int, payload: UniversityCreateInput, db: Session = Depends(get_db)):
    try:
        if not db.query(Teacher).filter(Teacher.id == teacher_id).first():
            raise HTTPException(status_code=404, detail="Teacher not found")
        
        uni = Universities(teacher_id=teacher_id, **payload.dict())
        db.add(uni)
        db.commit()
        return {"id": uni.id, "message": "University record added"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

# Preferences endpoint
@router.post("/teachers/{teacher_id}/preferences")
def add_preferences(teacher_id: int, payload: PreferenceCreateInput, db: Session = Depends(get_db)):
    try:
        if not db.query(Teacher).filter(Teacher.id == teacher_id).first():
            raise HTTPException(status_code=404, detail="Teacher not found")
        
        pref = Preferences(teacher_id=teacher_id, **payload.dict())
        db.add(pref)
        db.commit()
        return {"id": pref.id, "message": "Preferences added"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

# Preferred subjects endpoint
@router.post("/teachers/{teacher_id}/preferences/{preference_id}/subjects")
def add_preferred_subjects(teacher_id: int, preference_id: int, subjects: list[PreferredSubjectInput], db: Session = Depends(get_db)):
    try:
        pref = db.query(Preferences).filter(Preferences.id == preference_id, Preferences.teacher_id == teacher_id).first()
        if not pref:
            raise HTTPException(status_code=404, detail="Preference not found for this teacher")
        
        for subj in subjects:
            db.add(PreferredSubjects(preference_id=pref.id, **subj.dict()))
        db.commit()
        return {"message": f"{len(subjects)} preferred subject(s) added"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

# Preferred tuition types endpoint
@router.post("/teachers/{teacher_id}/preferences/{preference_id}/tuition-types")
def add_preferred_tuition_types(teacher_id: int, preference_id: int, tuition_types: list[PreferredTuitionTypeInput], db: Session = Depends(get_db)):
    try:
        pref = db.query(Preferences).filter(Preferences.id == preference_id, Preferences.teacher_id == teacher_id).first()
        if not pref:
            raise HTTPException(status_code=404, detail="Preference not found for this teacher")
        
        for tt in tuition_types:
            db.add(PreferredTuitionTypes(preference_id=pref.id, **tt.dict()))
        db.commit()
        return {"message": f"{len(tuition_types)} preferred tuition type(s) added"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

# Preferred time slots endpoint
@router.post("/teachers/{teacher_id}/preferences/{preference_id}/time-slots")
def add_preferred_time_slots(teacher_id: int, preference_id: int, time_slots: list[PreferredTimeSlotInput], db: Session = Depends(get_db)):
    try:
        pref = db.query(Preferences).filter(Preferences.id == preference_id, Preferences.teacher_id == teacher_id).first()
        if not pref:
            raise HTTPException(status_code=404, detail="Preference not found for this teacher")
        
        for ts in time_slots:
            db.add(PreferredTimeSlots(preference_id=pref.id, **ts.dict()))
        db.commit()
        return {"message": f"{len(time_slots)} preferred time slot(s) added"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

# Teaching type preferences endpoint
@router.post("/teachers/{teacher_id}/teaching-type-preferences")
def add_teaching_type_preferences(teacher_id: int, preferences: list[TeachingTypePreferenceInput], db: Session = Depends(get_db)):
    try:
        if not db.query(Teacher).filter(Teacher.id == teacher_id).first():
            raise HTTPException(status_code=404, detail="Teacher not found")
        
        for pref in preferences:
            db.add(TeachingTypePreferences(teacher_id=teacher_id, **pref.dict()))
        db.commit()
        return {"message": f"{len(preferences)} teaching type preference(s) added"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

# Admission preferences endpoint
@router.post("/teachers/{teacher_id}/admission-preferences")
def add_admission_preferences(teacher_id: int, preferences: list[AdmissionPreferenceInput], db: Session = Depends(get_db)):
    try:
        if not db.query(Teacher).filter(Teacher.id == teacher_id).first():
            raise HTTPException(status_code=404, detail="Teacher not found")
        
        for pref in preferences:
            db.add(AdmissionPreferences(teacher_id=teacher_id, **pref.dict()))
        db.commit()
        return {"message": f"{len(preferences)} admission preference(s) added"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

# Preferred areas endpoint
@router.post("/teachers/{teacher_id}/preferred-areas")
def add_preferred_areas(teacher_id: int, areas: list[PreferredAreaInput], db: Session = Depends(get_db)):
    try:
        if not db.query(Teacher).filter(Teacher.id == teacher_id).first():
            raise HTTPException(status_code=404, detail="Teacher not found")
        
        for area in areas:
            db.add(PreferredAreas(teacher_id=teacher_id, **area.dict()))
        db.commit()
        return {"message": f"{len(areas)} preferred area(s) added"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
