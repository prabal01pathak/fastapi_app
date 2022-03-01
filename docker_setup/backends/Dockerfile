FROM python:3.10.2-slim-buster as python_backend
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

WORKDIR /app
COPY ./backend/requirements.txt /app/backend/

RUN pip install gunicorn
RUN pip install -r backend/requirements.txt 
#ADD ./docker_setup /app/docker_setup/
ADD ./backend /app/backend 