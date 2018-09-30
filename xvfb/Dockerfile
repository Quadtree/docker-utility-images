FROM ubuntu
RUN apt-get update && apt-get install -y git xvfb nodejs npm firefox
RUN useradd -m cmp
USER cmp
RUN cd ~ ; npm install webdriver-manager
ENTRYPOINT ["/bin/bash"]