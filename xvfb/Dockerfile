FROM ubuntu
RUN apt-get update
RUN apt-get install -y git xvfb nodejs firefox npm
RUN npm -g install webdriver-manager
RUN useradd -m cmp
USER cmp
ENTRYPOINT ["/bin/bash"]