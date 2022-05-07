from fastapi import FastAPI

from db.db import DB
from routers import questions

DB.model.metadata.create_all(bind=DB.engine)

app = FastAPI()
app.include_router(questions.router)
