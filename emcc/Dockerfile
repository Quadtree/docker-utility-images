FROM ubuntu:23.04
RUN DEBIAN_FRONTEND=noninteractive apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y git xz-utils autoconf libtool make nano rsync pkg-config cmake python3 bison flex bzip2
RUN cd ~ && git clone https://github.com/juj/emsdk.git
ARG VERSION
RUN ~/emsdk/emsdk install $VERSION
RUN ~/emsdk/emsdk activate $VERSION
RUN echo 'source ~/emsdk/emsdk_env.sh' >> ~/.bashrc
ENTRYPOINT ["/bin/bash"]