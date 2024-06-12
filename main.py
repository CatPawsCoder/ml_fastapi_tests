from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel
from typing import Dict, Any


class Item(BaseModel):
    text: str


app = FastAPI()
classifier = pipeline("sentiment-analysis")


@app.get("/")
def root() -> Dict[str, str]:
    """
    Root endpoint that returns a welcome message.
    """
    return {"message": "Hello World"}


@app.post("/predict/")
def predict(item: Item) -> Dict[str, Any]:
    """
    Endpoint that returns the sentiment analysis of the provided text.
    """
    result = classifier(item.text)[0]
    return {"label": result['label'], "score": result['score']}


@app.get("/model_info/")
def model_info() -> Dict[str, str]:
    """
    Endpoint that returns the model information.
    """
    return {"model": "distilbert-base-uncased-finetuned-sst-2-english", "task": "sentiment-analysis"}


# Run this file to start the app: uvicorn app:app --reload

