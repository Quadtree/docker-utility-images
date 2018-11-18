FROM node:10

RUN apt-get update
RUN apt-get install -y python3
RUN npm install -g @angular/cli
RUN mkdir /www
RUN useradd -m cmp
RUN chown cmp:cmp /www
USER cmp

ENTRYPOINT ["/bin/bash"]