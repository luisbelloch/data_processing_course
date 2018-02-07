FROM debian:jessie-slim 
LABEL maintainer="Luis Belloch <docker@luisbelloch.es>"

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y build-essential python-software-properties python-pip python-dev && \
    pip install --upgrade setuptools && \
    rm -rf /var/lib/apt/lists/* ~/.cache/*

RUN pip install --upgrade apache-beam && \
    rm -rf ~/.cache/*

RUN mkdir -p /data /opt/beam
WORKDIR /opt/beam

