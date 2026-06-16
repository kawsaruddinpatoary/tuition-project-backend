from db import Base
from sqlalchemy import Column, Date, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

class Jobs(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, index=True)
    creator = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=False)
    relation_with_student = Column(Integer, ForeignKey('relationships.id'), nullable=False)
    description = Column(String(255), nullable=False)
    start_date = Column(Date, nullable=False)
    is_nagotiable = Column(Boolean, nullable=False)
    is_urgent = Column(Boolean, nullable=False)
    job_info = relationship("JobInfo", uselist=False, back_populates="job", cascade="all, delete-orphan")
    preferences = relationship("JobPreferences", uselist=False, back_populates="job", cascade="all, delete-orphan")
    relationship_rel = relationship("Relationships")

    
class JobInfo(Base):
    __tablename__ = 'job_info'

    job_id = Column(Integer, ForeignKey('jobs.id', ondelete='CASCADE'), primary_key=True, nullable=False)
    min_salary = Column(Integer, nullable=False)
    max_salary = Column(Integer, nullable=False)
    no_of_students = Column(Integer, nullable=False)
    days = Column(Integer, nullable=False)
    hours = Column(Integer, nullable=False)
    address = Column(Integer, ForeignKey('addresses.id'), nullable=False)
    institute_type = Column(Integer, ForeignKey('institute_types.id'), nullable=False)
    job = relationship("Jobs", uselist=False, back_populates="job_info")
    institute_type_rel = relationship("InstituteTypes")
    address_rel = relationship("Addresses")
    
    
class JobPreferences(Base):
    __tablename__ = 'job_preferences'

    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, ForeignKey('jobs.id', ondelete='CASCADE'), nullable=False)
    group = Column(Integer, ForeignKey('groups.id'), nullable=False)
    medium = Column(Integer, ForeignKey('mediums.id'), nullable=False)
    curriculum = Column(Integer, ForeignKey('curriculums.id'), nullable=False)
    gender = Column(Integer, ForeignKey('genders.id'), nullable=False)
    time = Column(Integer, ForeignKey('time_slots.id'), nullable=False)
    tuition_type = Column(Integer, ForeignKey('tuition_types.id'), nullable=False)
    area = Column(Integer, ForeignKey('areas.id'), nullable=False)
    job = relationship("Jobs", back_populates="preferences")
    group_rel = relationship("Groups")
    medium_rel = relationship("Mediums")
    curriculum_rel = relationship("Curriculums")
    gender_rel = relationship("Genders")
    time_rel = relationship("TimeSlots")
    tuition_type_rel = relationship("TuitionTypes")
    area_rel = relationship("Areas")
    subjects = relationship("SubjectJobPreferences", back_populates="job_preference", cascade="all, delete-orphan")

class SubjectJobPreferences(Base):
    __tablename__ = 'subject_job_preferences'

    id = Column(Integer, primary_key=True, index=True)
    preference_id = Column(Integer, ForeignKey('job_preferences.id', ondelete='CASCADE'), nullable=False)
    subject = Column(Integer, ForeignKey('subjects.id'), nullable=False)
    job_preference = relationship("JobPreferences", back_populates="subjects")
    subject_rel = relationship("Subjects")
    