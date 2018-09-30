FROM openjdk
RUN apt-get update && apt-get install -y git firefox python3
RUN pip3 install selenium
RUN useradd -m cmp
USER cmp
ENTRYPOINT ["/bin/bash"]