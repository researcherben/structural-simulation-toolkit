

# 
.PHONY: help 
help:
	@echo "make help"
	@echo "      this message"
	@echo "==== Targets outside container ===="
	@echo "make docker"
	@echo "      build and run docker"


.PHONY: docker docker_build docker_run
docker: docker_build docker_run
docker_build:
	docker build -f Dockerfile.phusion -t sst .
docker_run:
	docker run -it -v `pwd`:/scratch --rm sst /bin/bash

