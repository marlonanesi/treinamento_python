from fastapi import FastAPI
from pydantic import BaseModel
from api_client import get_feedback_from_openai

app = FastAPI()

class Evaluation(BaseModel):
    comment: str
    rating: int

@app.post("/feedback/")
async def feedback(evaluation: Evaluation):
    return get_feedback_from_openai(evaluation.comment, evaluation.rating)