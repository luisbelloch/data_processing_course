PHONY=build tag push list run

all: build requirements.txt tag

build:
	docker build -t luisbelloch/spark-jupyter .

requirements.txt: build
	docker run -t luisbelloch/spark-jupyter pip3 freeze > requirements.txt

tag:
	docker tag luisbelloch/spark-jupyter luisbelloch/spark-jupyter:2018.1

push:
	docker push luisbelloch/spark-jupyter:2018.1
	docker push luisbelloch/spark-jupyter

run:
	./pyspark-jupyter.sh

list:
	docker images luisbelloch/spark-jupyter

