from db import Base
from sqlalchemy import Column, Float, Integer, String, ForeignKey, Date, CheckConstraint
from sqlalchemy.orm import relationship
from models.common import Areas, EducationLevels, Boards, Groups, Mediums, Curriculums, Subjects, Genders, Religions, BloodGroups, Departments, Addresses, TuitionTypes, Classes

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    phone = Column(String(20), nullable=False)
    
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    user = relationship("User", back_populates="teacher_profile")
    personal = relationship("PersonalInfo", uselist=False, back_populates="teacher", cascade="all, delete-orphan")
    info = relationship("TeacherInfo", uselist=False, back_populates="teacher", cascade="all, delete-orphan")
    contacts = relationship("Contacts", uselist=False, back_populates="teacher", cascade="all, delete-orphan")
    schools = relationship("Schools", back_populates="teacher", cascade="all, delete-orphan")
    colleges = relationship("Colleges", back_populates="teacher", cascade="all, delete-orphan")
    universities = relationship("Universities", back_populates="teacher", cascade="all, delete-orphan")
    # Preferences and related many-to-many / one-to-one are defined in teacher_utils and referenced by string names
    teaching_type_preferences = relationship("TeachingTypePreferences", back_populates="teacher", cascade="all, delete-orphan")
    admission_preferences = relationship("AdmissionPreferences", back_populates="teacher", cascade="all, delete-orphan")
    preferred_areas = relationship("PreferredAreas", back_populates="teacher", cascade="all, delete-orphan")
    preferences = relationship("Preferences", back_populates="teacher", cascade="all, delete-orphan")
    
class PersonalInfo(Base):
    __tablename__ = 'personal_info'

    teacher_id = Column(Integer, ForeignKey('teachers.id', ondelete='CASCADE'), primary_key=True, nullable=False)
    father_name = Column(String(255), nullable=False)
    mother_name = Column(String(255), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    bio = Column(String(255), nullable=True)
    gender = Column(Integer, ForeignKey('genders.id'), nullable=False)
    religion = Column(Integer, ForeignKey('religions.id'), nullable=False)
    blood_group = Column(Integer, ForeignKey('blood_groups.id'), nullable=False)
    present_address = Column(Integer, ForeignKey('addresses.id'), nullable=False)
    permanent_address = Column(Integer, ForeignKey('addresses.id'), nullable=False)
    teacher = relationship("Teacher", back_populates="personal")
    present_address_rel = relationship("Addresses", foreign_keys=[present_address])
    permanent_address_rel = relationship("Addresses", foreign_keys=[permanent_address])
    gender_rel = relationship("Genders")
    religion_rel = relationship("Religions")
    blood_group_rel = relationship("BloodGroups")

class TeacherInfo(Base):
    __tablename__ = 'teacher_info'

    teacher_id = Column(Integer, ForeignKey('teachers.id', ondelete='CASCADE'), primary_key=True, nullable=False)
    group = Column(Integer, ForeignKey('groups.id'), nullable=False)
    medium = Column(Integer, ForeignKey('mediums.id'), nullable=False)
    curriculum = Column(Integer, ForeignKey('curriculums.id'), nullable=True)
    teacher = relationship("Teacher", back_populates="info")
    group_rel = relationship("Groups")
    medium_rel = relationship("Mediums")
    curriculum_rel = relationship("Curriculums")
    
class Contacts(Base):
    __tablename__ = 'contacts'

    teacher_id = Column(Integer, ForeignKey('teachers.id', ondelete='CASCADE'), primary_key=True, nullable=False)
    phone = Column(String(20), nullable=False)
    whatsapp_number = Column(String(20), nullable=True)
    secondary_phone = Column(String(20), nullable=True)
    teacher = relationship("Teacher", back_populates="contacts")


class Schools(Base):
    __tablename__ = 'schools'

    id = Column(Integer, primary_key=True, index=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id', ondelete='CASCADE'), nullable=False)
    name = Column(String(255), nullable=False)
    passing_year = Column(
        Integer, 
        CheckConstraint('passing_year >= 1800 AND passing_year <= 2100'), 
        nullable=False
    )
    grade = Column(Float, nullable=False)
    board = Column(Integer, ForeignKey('boards.id'), nullable=False)
    group = Column(Integer, ForeignKey('groups.id'), nullable=False)
    medium = Column(Integer, ForeignKey('mediums.id'), nullable=False)
    curriculum = Column(Integer, ForeignKey('curriculums.id'), nullable=False)
    teacher = relationship("Teacher", back_populates="schools")
    board_rel = relationship("Boards")
    group_rel = relationship("Groups")
    medium_rel = relationship("Mediums")
    curriculum_rel = relationship("Curriculums")


class Colleges(Base):
    __tablename__ = 'colleges'

    id = Column(Integer, primary_key=True, index=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id', ondelete='CASCADE'), nullable=False)
    name = Column(String(255), nullable=False)
    passing_year = Column(
        Integer, 
        CheckConstraint('passing_year >= 1800 AND passing_year <= 2100'), 
        nullable=False
    )
    grade = Column(Float, nullable=False)
    board = Column(Integer, ForeignKey('boards.id'), nullable=False)
    group = Column(Integer, ForeignKey('groups.id'), nullable=False)
    medium = Column(Integer, ForeignKey('mediums.id'), nullable=False)
    curriculum = Column(Integer, ForeignKey('curriculums.id'), nullable=False)
    teacher = relationship("Teacher", back_populates="colleges")
    board_rel = relationship("Boards")
    group_rel = relationship("Groups")
    medium_rel = relationship("Mediums")
    curriculum_rel = relationship("Curriculums")
    
class Universities(Base):
    __tablename__ = 'universities'

    id = Column(Integer, primary_key=True, index=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id', ondelete='CASCADE'), nullable=False)
    name = Column(String(255), nullable=False)
    passing_year = Column(
        Integer, 
        CheckConstraint('passing_year >= 1800 AND passing_year <= 2100'), 
        nullable=False
    )
    enroll_year = Column(
        Integer, 
        CheckConstraint('enroll_year >= 1800 AND enroll_year <= 2100'), 
        nullable=False
    )
    grade = Column(Float, nullable=False)
    department = Column(Integer, ForeignKey('departments.id'), nullable=False)
    level = Column(Integer, ForeignKey('education_levels.id'), nullable=False)
    teacher = relationship("Teacher", back_populates="universities")
    department_rel = relationship("Departments")
    level_rel = relationship("EducationLevels")
    
