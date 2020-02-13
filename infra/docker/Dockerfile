FROM openjdk:8-jdk-slim
LABEL maintainer="Luis Belloch <docker@luisbelloch.es>"

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y --no-install-recommends python3-software-properties python3-numpy curl && \
    rm -rf /var/lib/apt/lists/*

ARG SPARK_VERSION=2.4.5
ENV SPARK_HOME=/opt/spark
RUN mkdir -p /opt/spark && curl -s http://apache.rediris.es/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop2.7.tgz | tar -xz -C "${SPARK_HOME}" --strip-components=1
ENV PATH=$SPARK_HOME/bin:$SPARK_HOME/sbin:$PATH

RUN cp "${SPARK_HOME}/conf/log4j.properties.template" "${SPARK_HOME}/conf/log4j.properties" && \
    sed -ibak 's/rootCategory=INFO/rootCategory=ERROR/g' "${SPARK_HOME}/conf/log4j.properties"

ENV SPARK_NO_DAEMONIZE=true
ENV PYSPARK_PYTHON=python3
EXPOSE 4040 7077 8080

CMD ["pyspark"]

