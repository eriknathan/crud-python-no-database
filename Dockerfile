FROM python:3.9.16-slim-buster

LABEL authors="eriknathan"

RUN pip install python-dotenv

COPY ./database /database

COPY ./lib /lib

COPY main.py .

ENTRYPOINT ["python3", "main.py"]