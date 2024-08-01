FROM python:3.12-slim

ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app.py app.py
COPY boot.sh boot.sh

CMD ./boot.sh
