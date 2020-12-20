# Use baseimage-docker which is a modified Ubuntu specifically for Docker
# https://hub.docker.com/r/phusion/baseimage
# https://github.com/phusion/baseimage-docker
FROM phusion/baseimage:0.11

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

# Update and install packages
RUN apt update && apt -y upgrade && apt -y install \
	build-essential \
  python3-dev \
  python3-pip 

RUN pip3 install pybind11

# Clean up apt mess
RUN apt clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

