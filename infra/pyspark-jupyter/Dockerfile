FROM luisbelloch/spark
LABEL maintainer="Luis Belloch <docker@luisbelloch.es>"

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y --no-install-recommends python3-pip && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade setuptools wheel && \
    rm -rf ~/.cache/*

RUN pip3 install --upgrade jupyter pandas && \
    rm -rf ~/.cache/*

ENV PYSPARK_DRIVER_PYTHON=jupyter
ENV PYSPARK_DRIVER_PYTHON_OPTS="notebook --ip $(awk \'END{print $1}\' /etc/hosts) --allow-root --port 8888"

WORKDIR /opt/notebook
COPY entrypoint.sh /opt/notebook

EXPOSE 8888

CMD ["/opt/notebook/entrypoint.sh"]

