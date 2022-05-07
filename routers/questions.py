from typing import List

from fastapi import APIRouter, Depends, status
from pydantic import parse_obj_as

from public_api_requests import get_questions
from repositories.question import QuestionRepository
from schemas.question import QuestionModel

router = APIRouter(prefix="/questions", tags=["questions"])


@router.get("/", response_model=List[QuestionModel])
def list_questions(q_limit: int = 10, questions: QuestionRepository = Depends()):
    db_questions = questions.all(q_limit=q_limit)
    return parse_obj_as(List[QuestionModel], db_questions)


@router.post("/{question_num}", response_model=QuestionModel, status_code=status.HTTP_201_CREATED)
def request_questions(question_num: int, questions: QuestionRepository = Depends()):

    if question_num < 1:
        return []

    api_questions = get_questions(question_num)

    check_results = questions.check_questions(api_questions)
    while check_results["missing"] > 0:
        api_questions = get_questions(check_results["missing"])
        check_results = questions.check_questions(api_questions)

    return QuestionModel.from_orm(check_results["last_question"])
