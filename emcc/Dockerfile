FROM ubuntu:23.04
RUN DEBIAN_FRONTEND=noninteractive apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y git xz-utils autoconf libtool make nano rsync pkg-config cmake python3 bison flex bzip2
RUN useradd -m cmp
USER cmp
RUN cd ~ && git clone https://github.com/juj/emsdk.git
ARG VERSION
RUN ~/emsdk/emsdk install $VERSION
RUN ~/emsdk/emsdk activate $VERSION
RUN echo 'source ~/emsdk/emsdk_env.sh' >> ~/.bashrc
USER root
RUN mkdir /usr/local/znt_web /usr/local/znt_src
RUN chown cmp /usr/local/znt_web /usr/local/znt_src
USER cmp
ENTRYPOINT ["/bin/bash"]