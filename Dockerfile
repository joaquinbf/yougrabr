FROM alpine:3.11

RUN apk add --no-cache python3-dev gcc build-base && pip3 install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirement.txt