FROM ubuntu
RUN apt-get update && apt-get install -y git xvfb nodejs npm firefox
RUN useradd -m cmp
USER cmp
RUN cd ~ ; npm i webdriver-manager protractor
RUN echo 'export PATH="$PATH:/home/cmp/node_modules/.bin"' >> /home/cmp/.bashrc
RUN '/home/cmp/node_modules/.bin/webdriver-manager' update
ENTRYPOINT ["/bin/bash"]