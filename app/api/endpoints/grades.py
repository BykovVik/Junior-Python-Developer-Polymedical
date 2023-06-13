from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from api.db import get_db
from api.models import Grades
from api.schemas import GradeCreate, GradeBase, GradeOut

router = APIRouter()

@router.post("/grades", response_model=GradeOut)
async def create_grade(grade: GradeCreate, db: Session = Depends(get_db)):
    # test grades data
    grade_obj = Grades(
        grade = 10,
        student_id = None,
        course_id = None
    )
    db.add(grade_obj)
    db.commit()
    db.refresh(grade_obj)
    return grade_obj

@router.put("/grades/{grade_id}", response_model=GradeOut)
async def update_grade(grade_id: int, grade: GradeBase, db: Session = Depends(get_db)):
    grade_obj = db.query(Grades).filter(Grades.id == grade_id).first()
    if not grade_obj:
        raise HTTPException(status_code=404, detail="Grade not found")
    
    for field, value in grade.dict(exclude_unset=True).items():
        setattr(grade_obj, field, value)
        db.commit()
        db.refresh(grade_obj)
        return grade_obj