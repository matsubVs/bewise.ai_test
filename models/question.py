from sqlalchemy import Column, DateTime, Integer, String

from db.db import DB

Model = DB.model


class Question(Model):
    """Модель вопроса в базе данных"""
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, nullable=False)
    question_id = Column(Integer, index=True, unique=True)
    question = Column(String(255), nullable=False)
    answer = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False)
