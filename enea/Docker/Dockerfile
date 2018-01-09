FROM alpine
#FROM ubuntu
MAINTAINER nkolchenko@gmail.com

### Ubuntu
#RUN apt-get update
#RUN apt-get install -y curl
#RUN apt-get install -y  python
#RUN apt-get install -y  python-setuptools
#RUN apt-get install -y python-pip 
#RUN pip install --upgrade pip
#RUN pip install django

### alpine
RUN apk update
RUN apk add curl
RUN apk add bash
RUN apk add python3
RUN pip3 install django

### add helloworld_app itself with all the configs, etc.

ADD ./Compose/mysite /django_app

#WORKDIR /django_app
#CMD nohup python3 /django_app/manage.py runserver 0.0.0.0:8000 &

EXPOSE 8000:8000
