FROM openjdk:alpine
RUN apk update
RUN apk add ca-certificates openssl curl python3 nodejs nodejs-npm git
RUN update-ca-certificates
ADD build.py /tmp/build.py

RUN curl 'https://repo1.maven.org/maven2/com/google/javascript/closure-compiler/v20210505/closure-compiler-v20210505.jar' > /usr/local/bin/closure-compiler
RUN chmod +x /usr/local/bin/closure-compiler

RUN npm i -g clean-css-cli
RUN ln -s $(which cleancss) /usr/local/bin/cleancss
