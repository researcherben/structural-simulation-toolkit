

#
.PHONY: help
help:
	@echo "make help"
	@echo "      this message"
	@echo "==== Targets outside container ===="
	@echo "make docker_91"
	@echo "      build and run docker using SST v9.1"
	@echo "make docker_build_91"
	@echo "make docker_run_91"
	@echo "make docker_build_fresh_91"
	@echo "      do not use cached layers"
	@echo "make docker_10_core"
	@echo "      build and run docker using SST v10 core"
	@echo "make docker_10"
	@echo "      build and run docker using SST v10 core+elements"
	@echo "make docker_build_10"
	@echo "make docker_run_10"
	@echo "make docker_build_fresh_10"
	@echo "      do not use cached layers"
	@echo "make docker_head"
	@echo "      build and run docker using SST v10"
	@echo "make docker_build_head"
	@echo "make docker_run_head"
	@echo "make docker_build_fresh_head"
	@echo "      do not use cached layers"


.PHONY: docker_91 docker_build_91 docker_run_91
docker_91: docker_build_91 docker_run_91
docker_build_91:
	time docker build -f Dockerfile.phusion_9.1 -t sst_91 .
docker_run_91:
	docker run -it -v `pwd`:/scratch --rm sst_91 /bin/bash
docker_build_fresh_91:
	time docker build --no-cache -f Dockerfile.phusion_9.1 -t sst_91 .

.PHONY: docker_10 docker_build_10 docker_run_10
docker_10: docker_build_10 docker_run_10
docker_build_10:
	time docker build -f Dockerfile.phusion_10 -t sst_10 .
docker_run_10:
	docker run -it -v `pwd`:/scratch --rm sst_10 /bin/bash
docker_build_fresh_10:
	time docker build --no-cache -f Dockerfile.phusion_10 -t sst_10 .

.PHONY: docker_10_core docker_build_10_core docker_run_10_core
docker_10_core: docker_build_10_core docker_run_10_core
docker_build_10_core:
	time docker build -f Dockerfile.phusion_10_core -t sst_10_core .
docker_run_10_core:
	docker run -it -v `pwd`:/scratch --rm sst_10_core /bin/bash


.PHONY: docker_head docker_build_10 docker_run_head
docker_head: docker_build_head docker_run_head
docker_build_head:
	time docker build -f Dockerfile.phusion_head -t sst_head .
docker_run_head:
	docker run -it -v `pwd`:/scratch --rm sst_head /bin/bash
docker_build_fresh_head:
	time docker build --no-cache -f Dockerfile.phusion_head -t sst_head .


get_sst_source:
	mkdir sstsimulator
	cd sstsimulator/
	git clone https://github.com/sstsimulator/sst-elements.git
	git clone https://github.com/sstsimulator/sst-core.git
	git clone https://github.com/sstsimulator/sst-macro.git
	git clone https://github.com/sstsimulator/sst-external-element.git
	git clone https://github.com/sstsimulator/sst-tutorials.git
	git clone https://github.com/sstsimulator/sst-workbench.git
	git clone https://github.com/sstsimulator/sst-tools.git

