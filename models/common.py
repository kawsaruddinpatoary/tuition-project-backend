from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Date

class Areas(Base):
    __tablename__ = 'areas'

    id = Column(Integer, primary_key=True, index=True)
    area = Column(String(50), nullable=False)

class EducationLevels(Base):
    __tablename__ = 'education_levels'

    id = Column(Integer, primary_key=True, index=True)
    level = Column(String(50), nullable=False)

class Boards(Base):
    __tablename__ = 'boards'

    id = Column(Integer, primary_key=True, index=True)
    board = Column(String(50), nullable=False)

class Groups(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True, index=True)
    group = Column(String(50), nullable=False)
    

class Mediums(Base):
    __tablename__ = 'mediums'

    id = Column(Integer, primary_key=True, index=True)
    medium = Column(String(50), nullable=False)


class Curriculums(Base):
    __tablename__ = 'curriculums'

    id = Column(Integer, primary_key=True, index=True)
    curriculum = Column(String(50), nullable=False)

class Subjects(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String(50), nullable=False)

class Departments(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True, index=True)
    department = Column(String(50), nullable=False)

class Genders(Base):
    __tablename__ = 'genders'

    id = Column(Integer, primary_key=True, index=True)
    gender = Column(String(50), nullable=False)

class Religions(Base):
    __tablename__ = 'religions'

    id = Column(Integer, primary_key=True, index=True)
    religion = Column(String(50), nullable=False)

class BloodGroups(Base):
    __tablename__ = 'blood_groups'

    id = Column(Integer, primary_key=True, index=True)
    blood_group = Column(String(5), nullable=False)

class TuitionTypes(Base):
    __tablename__ = 'tuition_types'

    id = Column(Integer, primary_key=True, index=True)
    tuition_type = Column(String(50), nullable=False)

class TimeSlots(Base):
    __tablename__ = 'time_slots'

    id = Column(Integer, primary_key=True, index=True)
    time_slot = Column(String(50), nullable=False)

class Classes(Base):
    __tablename__ = 'classes'

    id = Column(Integer, primary_key=True, index=True)
    class_name = Column(String(50), nullable=False)
    
class Addresses(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True, index=True)
    division = Column(String(50), nullable=False)
    city = Column(String(50), nullable=False)
    area = Column(String(50), nullable=False)
    road = Column(String(50), nullable=False)
    building = Column(String(50), nullable=False)
    full_address = Column(String(255), nullable=False)

