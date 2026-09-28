# Sentiment API

API FastAPI per classificare il sentiment usando un modello DistilBERT pubblicato su Hugging Face Hub.

## Deploy

Il servizio viene eseguito su Render tramite Docker.

## Endpoint

- `GET /health`
- `POST /predict`

## Model revision

La versione del modello viene scelta tramite la variabile d'ambiente:

`MODEL_REVISION`
