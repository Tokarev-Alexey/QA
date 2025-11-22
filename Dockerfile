FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc g++ python3-dev && \
    rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

