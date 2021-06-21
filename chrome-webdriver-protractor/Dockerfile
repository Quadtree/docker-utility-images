FROM ubuntu:18.04
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y python3-pip npm chromium-browser default-jre yarn
RUN npm install -g protractor webdriver-manager
RUN webdriver-manager update
RUN useradd seluser
USER seluser