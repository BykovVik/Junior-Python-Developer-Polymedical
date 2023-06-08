from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session

from api.db import get_db
from api.models import Teachers
from api.schemas import TeacherOut

router = APIRouter()

@router.get("/teachers", response_model=List[TeacherOut])
async def get_teachers(db: Session = Depends(get_db)):
    teachers = db.query(Teachers).all()
    return teachers