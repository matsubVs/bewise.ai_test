from typing import Dict, List, Union

from fastapi.params import Depends
from sqlalchemy.orm import Session

from dependencies import get_db
from models.question import Question
from schemas.question import QuestionModel


class QuestionRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def all(self, q_limit: int = 100) -> List[Question]:
        query = self.db.query(Question)
        return query.limit(q_limit).all()

    def find(self, question_id: int) -> Question:
        query = self.db.query(Question)
        return query.filter(Question.question_id == question_id).first()

    def create(self, question: QuestionModel) -> Question:

        db_question = Question(
            question_id=question.question_id,
            question=question.question,
            answer=question.answer,
            created_at=question.created_at,
        )

        self.db.add(db_question)
        self.db.commit()
        self.db.refresh(db_question)

        return db_question

    def check_questions(self, questions: List[QuestionModel]) -> Dict[str, Union[int, QuestionModel]]:

        check_results = {"missing": 0, "last_question": None}

        for question in questions:
            if self.find(question.question_id):
                check_results["missing"] += 1
            else:
                check_results["last_question"] = self.create(question)

        return check_results
