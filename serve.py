
import os
import torch

from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSequenceClassification


MODEL_ID = "andrewczl/distilbert-imdb-sentiment"
MODEL_REVISION = os.getenv("MODEL_REVISION", "v1")

app = FastAPI()


tokenizer = AutoTokenizer.from_pretrained(
    MODEL_ID,
    revision=MODEL_REVISION
)

model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_ID,
    revision=MODEL_REVISION
)

model.eval()


class PredictionRequest(BaseModel):
    text: str


@app.get("/health")
def health():
    return {
        "status": "ok",
        "model": MODEL_ID,
        "revision": MODEL_REVISION
    }


@app.post("/predict")
def predict(request: PredictionRequest):

    inputs = tokenizer(
        request.text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=256
    )

    with torch.no_grad():
        outputs = model(**inputs)

    predicted_class = torch.argmax(
        outputs.logits,
        dim=-1
    ).item()

    label = "positive" if predicted_class == 1 else "negative"

    return {
        "text": request.text,
        "label": label,
        "class_id": predicted_class,
        "revision": MODEL_REVISION
    }
