from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import date

from api.db import get_db
from api.models import Students
from api.schemas import StudentCreate, StudentUpdate, StudentOut

router = APIRouter()


@router.post("/students", response_model=StudentOut)
async def create_student(student: StudentCreate, db: Session = Depends(get_db)):

    #test student data
    student_obj = Students(
        name= "Student",
        last_name = "Mony",
        birthdate = date(2000, 1, 1),
        email = "mony@gmail.com",
        phone = "+380509770976",
        group_id = None
    )
    db.add(student_obj)
    db.commit()
    db.refresh(student_obj)
    return student_obj


@router.get("/students/{student_id}", response_model=StudentOut)
async def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Students).filter(Students.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@router.put("/students/{student_id}", response_model=StudentOut)
async def update_student(student_id: int, student: StudentUpdate, db: Session = Depends(get_db)):
    student_obj = db.query(Students).filter(Students.id == student_id).first()
    if not student_obj:
        raise HTTPException(status_code=404, detail="Student not found")
    for field, value in student.dict(exclude_unset=True).items():
        setattr(student_obj, field, value)
    db.commit()
    db.refresh(student_obj)
    return student_obj


@router.delete("/students/{student_id}")
async def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Students).filter(Students.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(student)
    db.commit()
    return {"message": "Delete successful"}