from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from api.db import get_db
from api.models import Courses, Groups, Students
from api.schemas import CourseCreate, CourseOut, StudentOut

router = APIRouter()


@router.post("/courses", response_model=CourseOut)
async def create_course(course: CourseCreate, db: Session = Depends(get_db)):

    # test course data
    course_obj = Courses(
        course_name = "CS Course",
        teacher_id = None
    )
    db.add(course_obj)
    db.commit()
    db.refresh(course_obj)
    return course_obj


@router.get("/courses/{course_id}", response_model=CourseOut)
async def get_course(course_id: int, db: Session = Depends(get_db)):
    #Search for a course by id
    course = db.query(Courses).filter(Courses.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course


@router.get("/courses/{course_id}/students", response_model=List[StudentOut])
async def get_course_students(course_id: int, db: Session = Depends(get_db)):
    #Array to accumulate all students
    students_box = []
    #Search for a Groups by course id
    groupe = db.query(Groups).filter(Groups.id == course_id).all()
    if not groupe:
        raise HTTPException(status_code=404, detail="Group not found")
    
    #collect students from all found groups
    for g in groupe:
        students = db.query(Students).filter(g.id == Students.group_id).all()
        if len(students) > 1:
            for s in students:
                students_box.append(s)
        else:
            students_box.append(students[0])

    return students_box

    