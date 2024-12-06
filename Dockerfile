FROM python:3.10-slim

WORKDIR /app

# install build tools
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ app/
COPY run.py .

RUN mkdir -p models

EXPOSE 8080

ENV FLASK_APP=run.py
ENV FLASK_ENV=production
ENV WEBSITES_PORT=8080

CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:${WEBSITES_PORT:-8080} --timeout 120 --workers 4 run:app"]
