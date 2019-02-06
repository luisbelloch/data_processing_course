IMAGE_NAME:=luisbelloch/airflow
VERSION_TAG:=2019.1
DAG_VOLUME:=${PWD}/dags:/var/airflow/dags
WEB_PORT:=8080:8080

.PHONY: build
build:
	docker build -t $(IMAGE_NAME) .

.PHONY: tag
tag:
	docker tag ${IMAGE_NAME} ${IMAGE_NAME}:${VERSION_TAG}

.PHONY: push
push:
	docker push ${IMAGE_NAME}
	docker push ${IMAGE_NAME}:${VERSION_TAG}

.PHONY: web
web:
	docker run -p ${WEB_PORT} -v ${DAG_VOLUME} -ti $(IMAGE_NAME) airflow webserver

.PHONY: scheduler
scheduler:
	docker run -p ${WEB_PORT} -v ${DAG_VOLUME} -ti $(IMAGE_NAME) airflow scheduler

.PHONY: shell
shell:
	docker run -p ${WEB_PORT} -v ${DAG_VOLUME} -ti $(IMAGE_NAME) /bin/bash

