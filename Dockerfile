FROM python:3.7
WORKDIR /app
ADD . /app
ENV HTTP_PORT=8080
RUN python setup.py develop
EXPOSE 8080
