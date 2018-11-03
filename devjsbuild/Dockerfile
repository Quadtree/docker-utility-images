FROM openjdk:alpine
RUN apk update
RUN apk add ca-certificates openssl curl python3 nodejs nodejs-npm git
RUN update-ca-certificates
RUN curl 'https://sigma.quadtree.info:9443/default/devjsbuild/raw/master/build.py' > /tmp/build.py

RUN curl 'https://dl.google.com/closure-compiler/compiler-latest.zip' > /tmp/closure-compiler.zip
RUN mkdir /tmp/closure-compiler
RUN unzip /tmp/closure-compiler.zip -d /tmp/closure-compiler/
RUN mv /tmp/closure-compiler/*.jar /usr/local/bin/closure-compiler
RUN chmod +x /usr/local/bin/closure-compiler

RUN npm install

RUN npm install clean-css-cli -g
RUN which cleancss
RUN ln -s $(which cleancss) /usr/local/bin/cleancss
