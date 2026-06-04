from db import Base
from sqlalchemy import Column, Float, Integer, String, ForeignKey, Date, CheckConstraint
from sqlalchemy.orm import relationship
from models.common import Areas, EducationLevels, Boards, Groups, Mediums, Curriculums, Subjects, Departments, Classes, TuitionTypes, TimeSlots
from models.teachers import Teacher 

class TeachingTypes(Base):
    __tablename__ = 'teaching_types'

    id = Column(Integer, primary_key=True, index=True)
    teaching_type = Column('type', String(100), nullable=False)

class AdmissionTypes(Base):
    __tablename__ = 'admission_types'

    id = Column(Integer, primary_key=True, index=True)
    admission_type = Column(String(100), nullable=False)
    
class TeachingTypePreferences(Base):
    __tablename__ = 'teaching_type_preferences'

    teacher_id = Column(Integer, ForeignKey('teachers.id', ondelete='CASCADE'), primary_key=True, nullable=False)
    teaching_type = Column(Integer, ForeignKey('teaching_types.id', ondelete='CASCADE'), primary_key=True, nullable=False)
    teacher = relationship("Teacher", back_populates="teaching_type_preferences")
    teaching_type_rel = relationship("TeachingTypes")

class AdmissionPreferences(Base):
    __tablename__ = 'admission_preferences'

    teacher_id = Column(Integer, ForeignKey('teachers.id', ondelete='CASCADE'), primary_key=True, nullable=False)
    admission_type = Column(Integer, ForeignKey('admission_types.id', ondelete='CASCADE'), primary_key=True, nullable=False)
    teacher = relationship("Teacher", back_populates="admission_preferences")
    admission_type_rel = relationship("AdmissionTypes")
    
class PreferredAreas(Base):
    __tablename__ = 'preferred_areas'

    teacher_id = Column(Integer, ForeignKey('teachers.id', ondelete='CASCADE'), primary_key=True, nullable=False)
    area = Column(Integer, ForeignKey('areas.id', ondelete='CASCADE'), primary_key=True, nullable=False)
    teacher = relationship("Teacher", back_populates="preferred_areas")
    area_rel = relationship("Areas")

class Preferences(Base):
    __tablename__ = 'preferences'

    id = Column(Integer, primary_key=True, index=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id', ondelete='CASCADE'), nullable=False)
    min_salary = Column(Float, nullable=False)
    max_salary = Column(Float, nullable=False)
    group = Column(Integer, ForeignKey('groups.id'), nullable=False)
    medium = Column(Integer, ForeignKey('mediums.id'), nullable=False)
    curriculum = Column(Integer, ForeignKey('curriculums.id'), nullable=False)
    class_ = Column(Integer, ForeignKey('classes.id'), nullable=False)
    teacher = relationship("Teacher", back_populates="preferences")
    group_rel = relationship("Groups")
    medium_rel = relationship("Mediums")
    curriculum_rel = relationship("Curriculums")
    class_rel = relationship("Classes")
    preferred_subjects = relationship("PreferredSubjects", back_populates="preference", cascade="all, delete-orphan")
    preferred_tuition_types = relationship("PreferredTuitionTypes", back_populates="preference", cascade="all, delete-orphan")
    preferred_time_slots = relationship("PreferredTimeSlots", back_populates="preference", cascade="all, delete-orphan")

class PreferredSubjects(Base):
    __tablename__ = 'preferred_subjects'

    subject = Column(Integer, ForeignKey('subjects.id', ondelete='CASCADE'), primary_key=True, nullable=False)
    preference_id = Column(Integer, ForeignKey('preferences.id', ondelete='CASCADE'), primary_key=True, nullable=False)
    preference = relationship("Preferences", back_populates="preferred_subjects")
    subject_rel = relationship("Subjects")

class PreferredTuitionTypes(Base):
    __tablename__ = 'preferred_tuition_types'

    tuition_type = Column(Integer, ForeignKey('tuition_types.id', ondelete='CASCADE'), primary_key=True, nullable=False)
    preference_id = Column(Integer, ForeignKey('preferences.id', ondelete='CASCADE'), primary_key=True, nullable=False)
    preference = relationship("Preferences", back_populates="preferred_tuition_types")
    tuition_type_rel = relationship("TuitionTypes")

class PreferredTimeSlots(Base):
    __tablename__ = 'preferred_time_slots'

    time_slot = Column(Integer, ForeignKey('time_slots.id', ondelete='CASCADE'), primary_key=True, nullable=False)
    preference_id = Column(Integer, ForeignKey('preferences.id', ondelete='CASCADE'), primary_key=True, nullable=False)
    preference = relationship("Preferences", back_populates="preferred_time_slots")
    time_slot_rel = relationship("TimeSlots")

