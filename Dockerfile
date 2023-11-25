# Pull base image
FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1

# Set environment varibles
WORKDIR /app

# Install dependencies
COPY ./app/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --default-timeout=100 -r requirements.txt

COPY . /app

EXPOSE 80
