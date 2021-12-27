FROM python:3.10

COPY ./requirements.txt /app/requirements.txt
COPY ./main.py /app/main.py

RUN pip install -r /app/requirements.txt

COPY / /app

WORKDIR /app

EXPOSE 8000
