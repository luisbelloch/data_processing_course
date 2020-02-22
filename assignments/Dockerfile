FROM luisbelloch/spark
LABEL maintainer="Luis Belloch <docker@luisbelloch.es>"

WORKDIR /opt/tests/

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get upgrade -y python3 && \
    apt-get install -y --no-install-recommends python3-venv python3-pip && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip3 install wheel
RUN pip3 install -r requirements.txt

