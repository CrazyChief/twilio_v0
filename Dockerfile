FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /twilio_v0
WORKDIR /twilio_v0

RUN pip install --upgrade pip
ADD requirements.txt /twilio_v0/
RUN pip install -r requirements.txt
ADD . /twilio_v0/


