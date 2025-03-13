from fastapi import FastAPI
from pydantic import BaseModel
from api_client import get_feedback_from_openai
from mongodb import MongoDBConnection
from config import DATABASE_NAME
from kafka_producer import KafkaFeedbackProducer
from bson import ObjectId
from typing import List, Dict
import os

MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/')

app = FastAPI()
producer = KafkaFeedbackProducer()
class Evaluation(BaseModel):
    comment: str
    rating: int

class Feedback(BaseModel):
    id: str
    comment: str
    rating: int
    descricao: str = None
    status: str = None

# Initialize MongoDB connection
mongo_conn = MongoDBConnection(MONGO_URI, DATABASE_NAME)
db = mongo_conn.get_database()

@app.post("/feedback/")
async def feedback(evaluation: Evaluation):
    producer.produce_feedback(evaluation.dict())
    return {"status": "Enviado para o tópico kafka", "descricao": "Aguardando processamento"}

@app.get("/get-feedback/", response_model=List[Feedback])
async def get_feedback():
    feedback_collection = db["feedback"]
    feedbacks = feedback_collection.find().sort("_id", -1).limit(10)
    feedback_list = []

    for feedback in feedbacks:
        feedback_list.append({
            "id": str(feedback["_id"]),
            "comment": feedback["comment"],
            "rating": feedback["rating"],
            "descricao": feedback["descricao"],
            "status": feedback["status"]
        })
    return feedback_list