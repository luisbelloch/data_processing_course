AIRFLOW_VERSION:=2.4.3

.PHONY: all
all: clean docker-compose.yaml airflow init up

docker-compose.yaml:
	curl -LfO 'https://airflow.apache.org/docs/apache-airflow/${AIRFLOW_VERSION}/docker-compose.yaml'

airflow:
	curl -Lf 'https://airflow.apache.org/docs/apache-airflow/${AIRFLOW_VERSION}/airflow.sh' > airflow
	chmod +x airflow

.PHONY: init
init:
	docker-compose up airflow-init

.PHONY: up
up:
	docker-compose up

.PHONY: down
down:
	docker-compose down --remove-orphans

.PHONY: minio
minio:
	docker-compose -f docker-compose.yaml -f docker-compose.minio.yaml up minio

.PHONY: minio_connection
minio_connection: airflow
	./airflow connections import minio_connection.json

.PHONY: clean
clean:
	-docker-compose down --volumes --remove-orphans
	-rm -rf logs/ plugins/ .minio/ docker-compose.yaml airflow dags/__pycache__
