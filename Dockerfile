FROM python:3.9-slim-buster
MAINTAINER Abishek Tiwari <abhie.lp@gmail.com>

ENV INSTALL_PATH /snake_eyes
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN pip install -e .

CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "snake_eyes.app:create_app()"
