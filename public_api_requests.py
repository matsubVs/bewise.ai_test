from typing import List

import requests

from schemas.question import QuestionModel


def get_questions(count: int) -> List[QuestionModel]:
    req = requests.get("https://jservice.io/api/random?count=" + str(count))
    data = req.json()

    questions = []

    for question in data:
        question["question_id"] = question["id"]
        q_model = QuestionModel(**question)
        questions.append(q_model)

    return questions
