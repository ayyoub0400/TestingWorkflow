FROM ubuntu:latest

RUN apt-get update && apt-get install -y bash

COPY entrypoint.sh /app/entrypoint.sh

RUN chmod+x /app/entrypoint.sh

WORKDIR /app