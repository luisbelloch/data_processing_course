FROM debian:jessie-slim 
MAINTAINER Luis Belloch <docker@luisbelloch.es>

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y --no-install-recommends python-software-properties python-pip git && \
    pip install --upgrade pip setuptools && \
    rm -rf /var/lib/apt/lists/* ~/cache/pip/*

ENV BEAM_SETUP=/tmp/beam
RUN mkdir -p $BEAM_SETUP && \
    git clone https://github.com/apache/beam.git $BEAM_SETUP && \
    cd $BEAM_SETUP/sdks/python && \
    python setup.py sdist && \
    pip install dist/apache-beam-sdk-*.tar.gz && \
    rm -rf $BEAM_SETUP && \
    rm -rf ~/cache/pip/*

RUN mkdir -p /data /opt/beam
WORKDIR /opt/beam

