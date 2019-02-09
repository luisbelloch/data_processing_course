IMAGE_NAME:=luisbelloch/spark-assignments

.PHONY: all build tag push list test

test:
	./test.sh

all: build tag

build:
	docker build -t $(IMAGE_NAME) .

tag:
	docker tag $(IMAGE_NAME) $(IMAGE_NAME):2.4.0
	docker tag $(IMAGE_NAME) $(IMAGE_NAME):2019.1

push:
	docker push $(IMAGE_NAME):2.4.0
	docker push $(IMAGE_NAME):2019.1
	docker push $(IMAGE_NAME)

list:
	docker images $(IMAGE_NAME)
