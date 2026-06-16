from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session, selectinload
from typing import List
from db import get_db
from models.common import (Areas, EducationLevels, Boards, Groups, InstituteTypes, Mediums, Curriculums, Relationships, Subjects)
from models.job import Jobs, JobInfo, JobPreferences, SubjectJobPreferences
from schemas.common import (AreaCreate, AreaResponse, EducationLevelCreate, EducationLevelResponse,
                            BoardCreate, BoardResponse, GroupCreate, GroupResponse, InstituteTypeCreate,
                            InstituteTypeResponse, MediumCreate, MediumResponse, CurriculumCreate, CurriculumResponse,
                            RelationshipResponse, SubjectCreate, SubjectResponse)
from schemas.job import (JobCreate, JobCreateResponse, JobInfoCreate, JobPreferencesCreate, JobPreferencesResponse, JobResponse, SubjectJobPreferenceCreate)

router = APIRouter(prefix="/jobs", tags=["jobs"])

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

def serialize_jobinfo(job_info):
    if not job_info:
        return None
    return {
        "min_salary": job_info.min_salary,
        "max_salary": job_info.max_salary,
        "no_of_students": job_info.no_of_students,
        "days": job_info.days,
        "hours": job_info.hours,
        "address": serialize_address(job_info.address_rel),
        "institute_type": job_info.institute_type_rel.institute_type if getattr(job_info, "institute_type_rel", None) else None,
    }
    
def serialize_subject_job_preferences(subject_job_preference):
    if not subject_job_preference:
        return None
    return {
        "id": subject_job_preference.id,
        "preference_id": subject_job_preference.preference_id,
        "subject": subject_job_preference.subject_rel.subject if getattr(subject_job_preference, "subject_rel", None) else None,
    }

def serialize_jobpreferences(preferences):
    if not preferences:
        return None
    return {
        "id": preferences.id,
        "group": preferences.group_rel.group if getattr(preferences, "group_rel", None) else None,
        "medium": preferences.medium_rel.medium if getattr(preferences, "medium_rel", None) else None,
        "curriculum": preferences.curriculum_rel.curriculum if getattr(preferences, "curriculum_rel", None) else None,
        "gender": preferences.gender_rel.gender if getattr(preferences, "gender_rel", None) else None,
        "time": preferences.time_rel.time_slot if getattr(preferences, "time_rel", None) else None,
        "tuition_type": preferences.tuition_type_rel.tuition_type if getattr(preferences, "tuition_type_rel", None) else None,
        "area": preferences.area_rel.area if getattr(preferences, "area_rel", None) else None,
        "subjects": [
            serialize_subject_job_preferences(subject)
            for subject in preferences.subjects
        ] if preferences.subjects else []
    } 
    
    
def serialize_job(job):
    return {
        "id": job.id,
        "creator": job.creator,
        "email": job.email,
        "phone": job.phone,
        "relation_with_student": job.relationship_rel.relationship if getattr(job, "relationship_rel", None) else None,
        "description": job.description,
        "start_date": job.start_date,
        "is_nagotiable": job.is_nagotiable,
        "is_urgent": job.is_urgent,
        "job_info": serialize_jobinfo(job.job_info) if job.job_info else None,
        "preferences": serialize_jobpreferences(job.preferences) if job.preferences else None
    }


# Router setup

@router.post("")
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    db_job = Jobs(**job.dict())
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

@router.post("/{job_id}/info")
def create_job_info(job_id: int, job_info: JobInfoCreate, db: Session = Depends(get_db)):
    db_job_info = JobInfo(**job_info.dict(), job_id=job_id)
    db.add(db_job_info)
    db.commit()
    db.refresh(db_job_info)
    return serialize_jobinfo(db_job_info)

@router.post("/{job_id}/preferences")
def create_job_preferences(job_id: int, preferences: JobPreferencesCreate, db: Session = Depends(get_db)):
    db_preferences = JobPreferences(**preferences.dict(), job_id=job_id)
    db.add(db_preferences)
    db.commit()
    db.refresh(db_preferences)
    return serialize_jobpreferences(db_preferences)

@router.post("/{job_id}/preferences/{preference_id}/subjects")
def add_subject_to_job_preferences(job_id: int, preference_id: int, subject_preference: SubjectJobPreferenceCreate, db: Session = Depends(get_db)):
    db_subject_preference = SubjectJobPreferences(**subject_preference.dict(), preference_id=preference_id)
    db.add(db_subject_preference)
    db.commit()
    db.refresh(db_subject_preference)
    return serialize_subject_job_preferences(db_subject_preference)

@router.get("/{job_id}")
def get_job(job_id: int, db: Session = Depends(get_db)):
    db_job = db.query(Jobs).options(
        selectinload(Jobs.job_info),
        selectinload(Jobs.preferences).selectinload(JobPreferences.subjects).selectinload(SubjectJobPreferences.subject_rel),
    ).filter(Jobs.id == job_id).first()
    if not db_job:
        raise HTTPException(status_code=404, detail="Job not found")
    return serialize_job(db_job)

@router.get("")
def list_jobs(db: Session = Depends(get_db)):
    db_jobs = db.query(Jobs).options(
        selectinload(Jobs.job_info),
        selectinload(Jobs.preferences).selectinload(JobPreferences.subjects).selectinload(SubjectJobPreferences.subject_rel),
    ).all()
    return [serialize_job(job) for job in db_jobs]

@router.delete("/{job_id}")
def delete_job(job_id: int, db: Session = Depends(get_db)):
    db_job = db.query(Jobs).filter(Jobs.id == job_id).first()
    if not db_job:
        raise HTTPException(status_code=404, detail="Job not found")
    db.delete(db_job)
    db.commit()
    return {"detail": "Job deleted successfully"}

@router.put("/{job_id}")
def update_job(job_id: int, job_update: JobCreate, db: Session = Depends(get_db)):
    db_job = db.query(Jobs).filter(Jobs.id == job_id).first()
    if not db_job:
        raise HTTPException(status_code=404, detail="Job not found")
    for key, value in job_update.dict().items():
        setattr(db_job, key, value)
    db.commit()
    db.refresh(db_job)
    return serialize_job(db_job)

@router.put("/{job_id}/info")
def update_job_info(job_id: int, job_info_update: JobInfoCreate, db: Session = Depends(get_db)):
    db_job_info = db.query(JobInfo).filter(JobInfo.job_id == job_id).first()
    if not db_job_info:
        raise HTTPException(status_code=404, detail="Job info not found")
    for key, value in job_info_update.dict().items():
        setattr(db_job_info, key, value)
    db.commit()
    db.refresh(db_job_info)
    return serialize_jobinfo(db_job_info)

@router.put("/{job_id}/preferences")
def update_job_preferences(job_id: int, preferences_update: JobPreferencesCreate, db: Session = Depends(get_db)):
    db_preferences = db.query(JobPreferences).filter(JobPreferences.job_id == job_id).first()
    if not db_preferences:
        raise HTTPException(status_code=404, detail="Job preferences not found")
    for key, value in preferences_update.dict().items():
        setattr(db_preferences, key, value)
    db.commit()
    db.refresh(db_preferences)
    return serialize_jobpreferences(db_preferences)
