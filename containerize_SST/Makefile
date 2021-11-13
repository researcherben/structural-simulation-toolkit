

docker: docker_build docker_run
docker_build:
	docker build -t sst_11 .

docker_run:
	docker run --rm \
             -v `pwd`:/scratch \
             --user $(id -u):$(id -g) \
             sst_11 sst --version

singularity:
	singularity build sst_image.def