

# 
.PHONY: help 
help:
	@echo "make help"
	@echo "      this message"
	@echo "==== Targets outside container ===="
	@echo "make docker"
	@echo "      build and run docker"
	@echo "make docker_build"
	@echo "make docker_run"
	@echo "make docker_build_fresh"
	@echo "      do not use cached layers"


.PHONY: docker docker_build docker_run
docker: docker_build docker_run
docker_build:
	docker build -f Dockerfile.phusion -t sst .
docker_run:
	docker run -it -v `pwd`:/scratch --rm sst /bin/bash

docker_build_fresh:
	docker build --no-cache -f Dockerfile.phusion -t sst .

