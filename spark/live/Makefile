.PHONY: watch
watch:
	./live.sh

.PHONY: auth
auth:
	docker run -ti --name gcloud-config google/cloud-sdk gcloud auth login

.PHONY: set-project
set-project:
	./gcloud config set project bigdataupv2021

