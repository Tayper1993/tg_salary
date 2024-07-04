FROM python:3.12-slim
LABEL version="0.1.0" maintainer="Polyakov_KS"
ENV PYTHONUNBUFFERED=0
ENV LANG ru_RU.UTF-8

RUN apt-get update && apt-get -y install libpq-dev gcc git && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*

RUN /usr/local/bin/python -m pip install --upgrade pip

WORKDIR /usr/src/app
COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /code
COPY . /code

EXPOSE 8000
