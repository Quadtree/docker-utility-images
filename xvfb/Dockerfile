FROM ubuntu:20.04
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y git xvfb nodejs npm firefox openjdk-11-jdk
RUN useradd -m cmp
USER cmp
RUN cd ~ ; npm i webdriver-manager protractor
RUN echo 'export PATH="$PATH:/home/cmp/node_modules/.bin"' >> /home/cmp/.bashrc
RUN '/home/cmp/node_modules/.bin/webdriver-manager' update
ENTRYPOINT ["/bin/bash"]