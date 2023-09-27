FROM python:3.10-slim

USER root

WORKDIR /app

COPY ./core /app/core
COPY ./requirements.txt /app/requirements.txt
COPY ./main.py /app/main.py
COPY ./config.py /app/config.py

RUN apt -y update && apt -y upgrade
RUN pip install --upgrade pip
RUN apt-get -y install libpq-dev
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]