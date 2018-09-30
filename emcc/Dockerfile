FROM ubuntu
RUN apt-get update
RUN apt-get install -y git
RUN apt-get install -y python
RUN apt-get install -y xz-utils
RUN useradd -m cmp
USER cmp
RUN cd ~ && git clone https://github.com/juj/emsdk.git
RUN ~/emsdk/emsdk install latest
RUN ~/emsdk/emsdk activate latest
RUN echo 'source ~/emsdk/emsdk_env.sh' >> ~/.bashrc
USER root
RUN apt-get install -y autoconf
RUN apt-get install -y libtool
RUN apt-get install -y make
RUN apt-get install -y nano rsync
RUN apt-get install -y pkg-config
RUN mkdir /usr/local/znt_web /usr/local/znt_src
RUN chown cmp /usr/local/znt_web /usr/local/znt_src
USER cmp
ENTRYPOINT ["/bin/bash"]