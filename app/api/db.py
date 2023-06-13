from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://admin:Pan1cal_DEF_111@fastapi_db/fastapidb"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database handler
def get_db():

    db = SessionLocal()

    try:
        yield db
    except Exception as e:
        print(e)
    finally:
        db.close_all()

