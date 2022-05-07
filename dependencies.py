from sqlalchemy.orm import Session

from db.db import DB


def get_db() -> Session:
    db = DB.SessionLocal()
    try:
        yield db
    finally:
        db.close()
