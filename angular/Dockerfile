FROM node:10

RUN apt-get update
RUN apt-get install -y python3
RUN npm install -g @angular/cli
RUN useradd -m cmp
USER cmp

ENTRYPOINT ["/bin/bash"]