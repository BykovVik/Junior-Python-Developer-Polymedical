import uvicorn
from fastapi import FastAPI
from api.db import engine, Base, SessionLocal
from api.endpoints.teachers import router as TeacherRouter
from api.endpoints.students import router as StudentRouter
from api.endpoints.courses import router as CourseRouter
from api.endpoints.grades import router as GradeRouter


Base.metadata.create_all(bind=engine)
app = FastAPI()

# MAin Routing
app.include_router(StudentRouter)
app.include_router(TeacherRouter)
app.include_router(CourseRouter)
app.include_router(GradeRouter)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)