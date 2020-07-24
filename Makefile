

# 
.PHONY: help clean webserver typehints flake8 pylint doctest mccabe

help:
	@echo "make help"
	@echo "      this message"
	@echo "==== Targets outside container ===="
	@echo "make docker"
	@echo "      build and run docker"
	@echo "make dockerlive"
	@echo "      build and run docker /bin/bash"
	@echo "==== Targets inside container ===="

ifdef FILE_NAME
	@echo 'FILE_NAME is defined' $(FILE_NAME)
else
	@echo 'FILE_NAME is undefined'
endif

docker:
	docker build -f Dockerfile.phusion -t sst .
	docker run -it --rm sst

