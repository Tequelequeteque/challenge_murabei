FROM python:alpine

ENV DOCKERIZE_VERSION v0.7.0

RUN apk update --no-cache \
    && apk add --no-cache wget openssl \
    && wget -O - https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz | tar xzf - -C /usr/local/bin \
    && apk del wget

WORKDIR /server
COPY 00__database ../00__database
COPY . .
RUN pip install -r requirements/requirements.txt
CMD dockerize -wait tcp://${DB_HOST}:${DB_PORT} -timeout 30s python codes/main.py
