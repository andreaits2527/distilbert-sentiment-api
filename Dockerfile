FROM python:3.11-slim

WORKDIR /app

RUN useradd -m -u 1000 user

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY serve.py .

USER user

CMD ["sh", "-c", "uvicorn serve:app --host 0.0.0.0 --port ${PORT:-10000}"]
