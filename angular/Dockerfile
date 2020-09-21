FROM node:10

RUN DEBIAN_FRONTEND=noninteractive apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python3
RUN npm install -g @angular/cli
RUN mkdir /www
RUN useradd -m cmp
RUN chown cmp:cmp /www
USER cmp

CMD ["/bin/bash", "-c", "cd /www ; ng serve --watch --public-host sigma.quadtree.info --host 0.0.0.0"]