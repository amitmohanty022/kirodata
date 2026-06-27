FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/code/src \
    PORT=8000

WORKDIR /code

# Install the lightweight runtime first (API + mock model run without torch).
COPY requirements-dev.txt .
RUN pip install --no-cache-dir -r requirements-dev.txt uvicorn[standard]

COPY src ./src

EXPOSE 8000

CMD ["sh", "-c", "uvicorn optiscan.api:app --app-dir src --host 0.0.0.0 --port ${PORT}"]
