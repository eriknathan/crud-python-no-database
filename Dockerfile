FROM python:3.9.16-slim-buster

LABEL authors="eriknathan"

COPY ./database /database

COPY ./lib /app

COPY main.py /

ENTRYPOINT ["python3", "main.py"]