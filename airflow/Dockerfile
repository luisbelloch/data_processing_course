FROM python:3.6

ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux

RUN mkdir -p /var/airflow
ENV AIRFLOW_HOME=/var/airflow
ENV SLUGIFY_USES_TEXT_UNIDECODE=yes

RUN pip install --upgrade pip
RUN pip install apache-airflow
RUN airflow initdb

WORKDIR ${AIRFLOW_HOME}

