import uvicorn
from fastapi import FastAPI
from api.db import engine, Base, SessionLocal
from api.endpoints.teachers import router as TeacherRouter
from api.endpoints.students import router as StudentRouter 


Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(StudentRouter)
app.include_router(TeacherRouter)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)