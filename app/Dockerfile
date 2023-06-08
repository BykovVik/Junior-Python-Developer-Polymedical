FROM python:3.9-buster

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
CMD alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000
