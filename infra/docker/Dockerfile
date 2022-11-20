FROM amazoncorretto:11 as corretto-jdk
RUN $JAVA_HOME/bin/jlink \
    --verbose \
    --add-modules ALL-MODULE-PATH \
    --strip-debug \
    --no-man-pages \
    --no-header-files \
    --compress=2 \
    --output /opt/jre

FROM debian:stable-slim
LABEL maintainer="Luis Belloch <docker@luisbelloch.es>"
ENV JAVA_HOME=/opt/jre
ENV PATH="${JAVA_HOME}/bin:${PATH}"
COPY --from=corretto-jdk /opt/jre $JAVA_HOME

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y --no-install-recommends ca-certificates procps python3-software-properties python3-numpy curl && \
    rm -rf /var/lib/apt/lists/*

ARG SPARK_VERSION=3.3.1
ENV SPARK_HOME=/opt/spark
RUN mkdir -p /opt/spark && curl -s https://downloads.apache.org/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop3.tgz | tar -xz -C "${SPARK_HOME}" --strip-components=1
ENV PATH="${SPARK_HOME}/bin:${SPARK_HOME}/sbin:${PATH}"

RUN cp "${SPARK_HOME}/conf/log4j2.properties.template" "${SPARK_HOME}/conf/log4j2.properties" && \
    sed -ibak 's/rootLogger.level = info/rootLogger.level = error/g' "${SPARK_HOME}/conf/log4j2.properties"

ENV SPARK_NO_DAEMONIZE=true
ENV PYSPARK_PYTHON=/usr/bin/python3
ENV PYSPARK_DRIVER_PYTHON=/usr/bin/python3
EXPOSE 4040 7077 8080

CMD ["pyspark"]
