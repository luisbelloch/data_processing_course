PHONY=build tag push list

all: build tag

build:
	docker build -t luisbelloch/beam .

tag:
	docker tag luisbelloch/beam luisbelloch/beam:2018.1

push:
	docker push luisbelloch/beam:2018.1
	docker push luisbelloch/beam

list:
	docker images luisbelloch/beam

