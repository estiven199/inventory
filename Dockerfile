FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV PORT 8000

CMD exec uvicorn main:app --host 0.0.0.0 --port $PORT