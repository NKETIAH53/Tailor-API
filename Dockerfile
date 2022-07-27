FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt

# RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev \
# pip-compile requirements.in && pip-sync requirements.txt

RUN pip install -r requirements.txt