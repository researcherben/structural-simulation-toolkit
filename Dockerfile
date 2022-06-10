# Use baseimage-docker which is a modified Ubuntu specifically for Docker
# https://hub.docker.com/r/phusion/baseimage
# https://github.com/phusion/baseimage-docker
FROM phusion/baseimage:0.11

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

# Update and install packages
RUN apt update && apt -y upgrade && apt -y install \
	build-essential \
	git \
	libtool-bin \
  valgrind \
  doxygen \
  graphviz \
  time \
	mpich \
  python3-dev \
  python3-pip \
	automake 

RUN pip3 install pybind11 makefile2dot

# Clean up apt mess
RUN apt clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Setup Environment for SST
ARG dir=/home/sst/build
RUN mkdir -p $dir
ARG SST_CORE_HOME=/home/sst/sst-core
ENV SST_CORE_HOME=/home/sst/sst-core
ENV PATH="$PATH:$SST_CORE_HOME/bin"

# Clone the repos from GitHub
#RUN git clone https://github.com/sstsimulator/sst-core.git $dir/sst-core

WORKDIR $dir

# from https://github.com/sstsimulator/sst-core/releases/tag/v10.0.0_Final
COPY sstcore-11.0.0.tar.gz .
RUN tar zxvf sstcore-11.0.0.tar.gz
RUN mv sstcore-11.0.0 sst-core

# Build SST Core
RUN cd $dir/sst-core && ./autogen.sh && \
	./configure --prefix=$SST_CORE_HOME && \
	make all install

WORKDIR /home/sst/

# the following file needs to be writable to register components
RUN chmod g+rwx /home/sst/sst-core/etc/sst/sstsimulator.conf
RUN chmod o+rwx /home/sst/sst-core/etc/sst/sstsimulator.conf


# Clean up SST junk
#RUN rm -rf $dir
