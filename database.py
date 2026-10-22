from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# DATABASE_URL ="mysql+pymysql://root:root@localhost:3306/my_project_exercise"
DATABASE_URL = "postgresql+psycopg2://mydatabase_co42_user:3mt3QqbPPtiPLiqlWF3oGooLmhHFjqkm@dpg-dbcumh7avr4c738si140-a.oregon-postgres.render.com/mydatabase_co42"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()