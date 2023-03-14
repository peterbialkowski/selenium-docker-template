# syntax=docker/dockerfile:1

FROM python:3.10-slim
WORKDIR /app
COPY sel_docker .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt 
CMD [ "python3", "/app/main.py" ]
