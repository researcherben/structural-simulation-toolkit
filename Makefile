

# 
.PHONY: help 
help:
	@echo "make help"
	@echo "      this message"
	@echo "==== Targets outside container ===="
	@echo "make docker_"
	@echo "      build and run docker using SST v9.1"
	@echo "make docker_build_91"
	@echo "make docker_run_91"
	@echo "make docker_build_fresh_91"
	@echo "      do not use cached layers"
	@echo "make docker_10"
	@echo "      build and run docker using SST v10"
	@echo "make docker_build_10"
	@echo "make docker_run_10"
	@echo "make docker_build_fresh_10"
	@echo "      do not use cached layers"


.PHONY: docker_91 docker_build_91 docker_run_91
docker_91: docker_build_91 docker_run_91
docker_build_91:
	docker build -f Dockerfile.phusion_9.1 -t sst_91 .
docker_run_91:
	docker run -it -v `pwd`:/scratch --rm sst_91 /bin/bash
docker_build_fresh_91:
	docker build --no-cache -f Dockerfile.phusion_91 -t sst_91 .

.PHONY: docker_10 docker_build_10 docker_run_10
docker_10: docker_build_10 docker_run_10
docker_build_10:
	docker build -f Dockerfile.phusion_10 -t sst_10 .
docker_run_10:
	docker run -it -v `pwd`:/scratch --rm sst_10 /bin/bash
docker_build_fresh_10:
	docker build --no-cache -f Dockerfile.phusion_10 -t sst_10 .

