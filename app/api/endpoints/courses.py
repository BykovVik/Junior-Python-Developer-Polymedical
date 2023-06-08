from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from api.db import get_db
from api.models import Courses
from api.schemas import CourseCreate, CourseOut

router = APIRouter()


@router.post("/courses", response_model=CourseOut)
async def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    course_obj = Courses(**course.dict())
    db.add(course_obj)
    db.commit()
    db.refresh(course_obj)
    return course_obj


@router.get("/courses/{course_id}", response_model=CourseOut)
async def get_course(course_id: int, db: Session = Depends(get_db)):
    course = db.query(Courses).filter(Courses.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course


@router.get("/courses/{course_id}/students", response_model=List[CourseOut])
async def get_course_students(course_id: int, db: Session = Depends(get_db)):
    course = db.query(Courses).filter(Courses.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course.students