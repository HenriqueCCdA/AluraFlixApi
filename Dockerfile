FROM python:3.10.8-alpine3.16

ARG USER_DIR=/user/app

# set work directory
WORKDIR $USER_DIR

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy project
COPY aluraflix_api/ ./aluraflix_api
COPY manage.py ./
COPY requirements.txt ./

# install dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
