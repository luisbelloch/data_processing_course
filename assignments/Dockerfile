FROM luisbelloch/spark
LABEL maintainer="Luis Belloch <docker@luisbelloch.es>"

WORKDIR /opt/tests/

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y --no-install-recommends python3-venv && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN python3 -m venv .venv
ENV PATH="/opt/tests/.venv/bin:${PATH}"
RUN pip install wheel
RUN pip install -r requirements.txt

