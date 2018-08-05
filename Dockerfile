FROM ubuntu
RUN apt-get update
RUN apt-get install -y git emscripten
RUN useradd -m cmp
USER cmp
ENTRYPOINT ["/bin/bash"]