

docker: docker_build docker_run
docker_build:
	docker build -t sst_11 .

docker_run:
	docker run -it --rm \
             -v `pwd`:/scratch \
             --user $(id -u):$(id -g) \
             sst_11 /bin/bash 

apptainer: apptainer_build apptainer_shell

apptainer_build:
	apptainer build sst_image.sif sst_image.def

apptainer_shell:
	apptainer shell sst_image.sif

viz_Makefile:
	makefile2dot | dot -Tpng > Makefile_viz.png
