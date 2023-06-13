from typing import List, Union
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
    # TODO: Add Groups Scheme
    # groups: List["GroupsOut"] = []

    class Config:
        orm_mode = True


class TeacherBase(BaseModel):
    name: str
    last_name: str
    birthdate: date
    email: str
    phone: str

class TeacherOut(TeacherBase):
    id: int
    courses: List["CourseOut"] = []

    class Config:
        orm_mode = True


class CourseBase(BaseModel):
    course_name: str


class CourseCreate(CourseBase):
    teacher_id: Union[int, None]

class CourseOut(CourseBase):
    id: int
    teacher: Union[List[TeacherOut], None] = []
    grades: List["GradeOut"] = []

    class Config:
        orm_mode = True


class GradeBase(BaseModel):
    grade: int


class GradeCreate(GradeBase):
    student_id: Union[int, None]
    course_id: Union[int, None]


class GradeOut(GradeBase):
    id: int
    student: Union[List[StudentOut], None] = []
    course: Union[List[CourseOut], None] = []

    class Config:
        orm_mode = True


StudentOut.update_forward_refs()
TeacherOut.update_forward_refs()
CourseOut.update_forward_refs()
GradeOut.update_forward_refs()