from sqlalchemy import Column, Integer, String, Date, ForeignKey, Text, Time
from sqlalchemy.orm import relationship
from api.db import Base


class Departments(Base):
    __tablename__ = 'Departments'

    id = Column(Integer, primary_key=True)
    departments_name = Column(String(255), nullable=False)

class Buildings(Base):
    __tablename__ = 'Buildings'

    id = Column(Integer, primary_key=True)
    building_name = Column(String(255), nullable=False)

class Teachers(Base):
    __tablename__ = 'Teachers'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    birthdate = Column(Date, nullable=False)
    email = Column(String(255), nullable=False)
    phone = Column(String(255), nullable=False)

class Courses(Base):
    __tablename__ = 'Courses'

    id = Column(Integer, primary_key=True)
    course_name = Column(String(255), nullable=False)
    teacher_id = Column(Integer, ForeignKey('Teachers.id'), nullable=True)
    teacher = relationship(Teachers)

class CoursePrograms(Base):
    __tablename__ = 'CoursePrograms'

    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey('Courses.id'), nullable=False)
    description = Column(Text, nullable=False)

class Curriculum(Base):
    __tablename__ = 'Curriculum'

    id = Column(Integer, primary_key=True)
    specialty_name = Column(String(255), nullable=False)
    year_of_study = Column(Date, nullable=False)
    course_id = Column(Integer, ForeignKey('Courses.id'), nullable=False)

class Groups(Base):
    __tablename__ = 'Groups'

    id = Column(Integer, primary_key=True)
    group_name = Column(String(255), nullable=False)
    course_id = Column(Integer, ForeignKey('Courses.id'), nullable=False)
    departments_id = Column(Integer, ForeignKey('Departments.id'), nullable=False)
    courses = relationship(Courses)

class Students(Base):
    __tablename__ = 'Students'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    birthdate = Column(Date, nullable=False)
    email = Column(String(255), nullable=False)
    phone = Column(String(255), nullable=False)
    group_id = Column(Integer, ForeignKey('Groups.id'), nullable=True)
    groups = relationship(Groups)

class Grades(Base):
    __tablename__ = 'Grades'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('Students.id'), nullable=True)
    course_id = Column(Integer, ForeignKey('Courses.id'), nullable=True)
    grade = Column(Integer, nullable=False)

class Classrooms(Base):
    __tablename__ = 'Classrooms'

    id = Column(Integer, primary_key=True)
    classroom_number = Column(Integer, nullable=False)
    building_id = Column(Integer, ForeignKey('Buildings.id'), nullable=False)
    buildings = relationship(Buildings)

class Exams(Base):
    __tablename__ = 'Exams'

    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey('Courses.id'), nullable=False)
    date = Column(Date, nullable=False)
    classrooms_id = Column(Integer, ForeignKey('Classrooms.id'), nullable=False)
    classrooms = relationship(Classrooms)

class Schedule(Base):
    __tablename__ = 'Schedule'

    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, ForeignKey('Groups.id'), nullable=False)
    day = Column(Date, nullable=False)
    begin_lessons = Column(Time, nullable=False)
    end_lessons = Column(Time, nullable=False)
    classroom_id = Column(Integer, ForeignKey('Classrooms.id'), nullable=False)
    classrooms = relationship(Classrooms)
    teacher_id = Column(Integer, ForeignKey('Teachers.id'), nullable=False)
    teachers = relationship(Teachers)

class Faculties(Base):
    __tablename__ = 'Faculties'

    id = Column(Integer, primary_key=True)
    faculties_name = Column(String(255), nullable=False)
    departments_id = Column(Integer, ForeignKey('Departments.id'), nullable=False)
    departments = relationship(Departments)

class Homeworks(Base):
    __tablename__ = 'Homeworks'

    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey('Courses.id'), nullable=False)
    description = Column(Text, nullable=False)