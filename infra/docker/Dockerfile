FROM openjdk:8-jdk-slim
MAINTAINER Luis Belloch <docker@luisbelloch.es>

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends python3-software-properties curl && rm -rf /var/lib/apt/lists/*

ENV SPARK_HOME=/opt/spark
RUN mkdir -p /opt/spark && curl -s http://apache.rediris.es/spark/spark-2.2.1/spark-2.2.1-bin-hadoop2.7.tgz | tar -xz -C "${SPARK_HOME}" --strip-components=1
ENV PATH=$SPARK_HOME/bin:$SPARK_HOME/sbin:$PATH

ENV SPARK_NO_DAEMONIZE=true
ENV PYSPARK_PYTHON=python3
EXPOSE 4040 7077 8080

CMD ["pyspark"]

