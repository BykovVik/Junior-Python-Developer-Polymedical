from typing import List
from datetime import date
from pydantic import BaseModel


class StudentBase(BaseModel):
    name: str
    last_name: str
    birthdate: date
    email: str
    phone: str


class StudentCreate(StudentBase):
    group_id: int


class StudentUpdate(StudentBase):
    pass


class StudentDeleteResponse(BaseModel):
    result: bool


class StudentOut(StudentBase):
    id: int
    courses: List["CourseOut"] = []

    class Config:
        orm_mode = True


class TeacherBase(BaseModel):
    name: str
    last_name: str
    birthdate: date
    email: str
    phone: str


class TeacherCreate(TeacherBase):
    pass


class TeacherUpdate(TeacherBase):
    pass


class TeacherDeleteResponse(BaseModel):
    result: bool


class TeacherOut(TeacherBase):
    id: int
    courses: List["CourseOut"] = []

    class Config:
        orm_mode = True


class CourseBase(BaseModel):
    course_name: str


class CourseCreate(CourseBase):
    teacher_id: int


class CourseOut(CourseBase):
    id: int
    teacher: TeacherOut
    students: List[StudentOut] = []
    grades: List["GradeOut"] = []

    class Config:
        orm_mode = True


class GradeBase(BaseModel):
    grade: int


class GradeCreate(GradeBase):
    student_id: int
    course_id: int


class GradeOut(GradeBase):
    id: int
    student: StudentOut
    course: CourseOut

    class Config:
        orm_mode = True


StudentOut.update_forward_refs()
TeacherOut.update_forward_refs()
CourseOut.update_forward_refs()
GradeOut.update_forward_refs()