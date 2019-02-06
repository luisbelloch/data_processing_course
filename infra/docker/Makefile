.PHONY: all build tag push list

all: build tag

build:
	docker build -t luisbelloch/spark .

tag:
	docker tag luisbelloch/spark luisbelloch/spark:2.4.0
	docker tag luisbelloch/spark luisbelloch/spark:2019.1

push:
	docker push luisbelloch/spark:2.4.0
	docker push luisbelloch/spark:2019.1
	docker push luisbelloch/spark

list:
	docker images luisbelloch/spark

