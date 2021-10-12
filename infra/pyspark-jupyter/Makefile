.PHONY: build tag push list run

all: build tag

build:
	docker build -t luisbelloch/pyspark-jupyter .

tag:
	docker tag luisbelloch/pyspark-jupyter luisbelloch/pyspark-jupyter:2021.10

push:
	docker push luisbelloch/pyspark-jupyter:2021.10
	docker push luisbelloch/pyspark-jupyter

run:
	docker run -p 8888:8888 -p 4040:4040 luisbelloch/pyspark-jupyter

list:
	docker images luisbelloch/pyspark-jupyter

