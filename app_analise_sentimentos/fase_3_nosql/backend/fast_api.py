from fastapi import FastAPI
from pydantic import BaseModel
from api_client import get_feedback_from_openai
from mongodb import MongoDBConnection

app = FastAPI()

class Evaluation(BaseModel):
    comment: str
    rating: int

# Initialize MongoDB connection
mongo_conn = MongoDBConnection("mongodb://localhost:27017/", "local")
db = mongo_conn.get_database()

@app.post("/feedback/")
async def feedback(evaluation: Evaluation):
    response = get_feedback_from_openai(evaluation.comment, evaluation.rating)
    
    # Save response to MongoDB
    feedback_collection = db["feedback"]
    feedback_collection.insert_one({
        "comment": evaluation.comment,
        "rating": evaluation.rating,
        "response": response
    })
    
    return response

