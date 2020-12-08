SPARK_VERSION:=3.0.1
COURSE_VERSION:=2020.12
IMAGE_NAME:=luisbelloch/spark

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(lastword $(MAKEFILE_LIST)) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: all
all: build tag ## Builds and tags an image

.PHONY: build
build: ## Assembles image from Spark binaries
	docker build --build-arg SPARK_VERSION=${SPARK_VERSION} -t $(IMAGE_NAME) .

.PHONY: tag
tag: ## Adds tags to current latest image
	docker tag $(IMAGE_NAME) $(IMAGE_NAME):$(SPARK_VERSION)
	docker tag $(IMAGE_NAME) $(IMAGE_NAME):$(COURSE_VERSION)

.PHONY: push
push: ## Uploads images to registry
	docker push $(IMAGE_NAME):$(SPARK_VERSION)
	docker push $(IMAGE_NAME):$(COURSE_VERSION)
	docker push $(IMAGE_NAME)

.PHONY: list
list: ## Lists local generated images
	docker images $(IMAGE_NAME)

