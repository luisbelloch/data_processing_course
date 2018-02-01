PHONY=build tag push list

all: build tag

build:
	docker build -t luisbelloch/spark .

tag:
	docker tag luisbelloch/spark luisbelloch/spark:2.2.1
	docker tag luisbelloch/spark luisbelloch/spark:2018.1

push:
	docker push luisbelloch/spark:2.2.1 
	docker push luisbelloch/spark:2018.1
	# docker push luisbelloch/spark

list:
	docker images luisbelloch/spark

