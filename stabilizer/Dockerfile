# Use baseimage-docker which is a modified Ubuntu specifically for Docker
# https://hub.docker.com/r/phusion/baseimage
# https://github.com/phusion/baseimage-docker
FROM phusion/baseimage:0.11

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

# Update and install packages
RUN apt update && apt -y upgrade && apt -y install \
    build-essential \
    doxygen \
    libtool-bin \
    git \
    graphviz \
    time \
    mpich \
    python3-dev \
    python3-pip \
    automake \
    cmake

# Clean up apt mess
RUN apt clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# this does not install clang++
#RUN apt -y install libclang1-6.0

# build from source as per https://clang.llvm.org/get_started.html
WORKDIR /opt/
RUN git clone https://github.com/llvm/llvm-project.git
WORKDIR /opt/llvm-project
RUN mkdir build
WORKDIR /opt/llvm-project/build
RUN cmake -DLLVM_ENABLE_PROJECTS=clang -G "Unix Makefiles" ../llvm
# errors with message
# CMake 3.13.4 or higher is required.  You are running version 3.10.2
RUN make


# https://github.com/ccurtsinger/stabilizer
WORKDIR /opt/
RUN git clone https://github.com/ccurtsinger/stabilizer.git
WORKDIR /opt/stabilizer
RUN make

ARG USER=sst
ARG UID=1000
ARG GID=1000
# default password for user
ARG PW=sst

RUN useradd -m ${USER} --uid=${UID} && echo "${USER}:${PW}" | chpasswd

#USER ${UID}:${GID}
WORKDIR /home/${USER}



# Setup Environment for SST
ARG dir=/home/sst/build
RUN mkdir -p $dir
ARG SST_CORE_HOME=/home/sst/sst-core
ENV SST_CORE_HOME=/home/sst/sst-core
ENV PATH="$PATH:$SST_CORE_HOME/bin"

WORKDIR $dir

# from https://github.com/sstsimulator/sst-core/releases/tag/v10.0.0_Final
COPY sstcore-10.0.0.tar.gz .
RUN tar zxvf sstcore-10.0.0.tar.gz
RUN mv sstcore-10.0.0 sst-core

# Build SST Core
#RUN cd $dir/sst-core && ./autogen.sh && \
#  	./configure --prefix=$SST_CORE_HOME && \
#	  make all install



WORKDIR /home/sst/

# Clean up SST junk
#RUN rm -rf $dir
