.PHONY: all build tag push list run

all: build requirements.txt tag

build:
	docker build -t luisbelloch/pyspark-jupyter .

requirements.txt: build
	docker run -t luisbelloch/pyspark-jupyter pip3 freeze > requirements.txt

tag:
	docker tag luisbelloch/pyspark-jupyter luisbelloch/pyspark-jupyter:2019.1

push:
	docker push luisbelloch/pyspark-jupyter:2019.1
	docker push luisbelloch/pyspark-jupyter

run:
	./pyspark-jupyter.sh

list:
	docker images luisbelloch/pyspark-jupyter

