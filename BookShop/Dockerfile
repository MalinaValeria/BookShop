#pull official base image
FROM python:3.10-slim

#set work directory
WORKDIR /usr/src/app

#set environment variables
#PYTHONDONTWRITEBYTECODE означает, что Python не будет пытаться создавать файлы .pyc
#PYTHONUNBUFFERED гарантирует, что наш вывод консоли выглядит знакомым и не буферизируется Docker
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && apt install -y gcc

#install dependencies
COPY requirements.txt ./requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

#copy project
COPY . .