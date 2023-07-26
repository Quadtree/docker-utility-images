FROM ubuntu:23.04
RUN DEBIAN_FRONTEND=noninteractive apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python3-pip npm default-jre curl git libgconf-2-4
RUN curl 'https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb' > /tmp/chrome.deb
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y /tmp/chrome.deb
RUN npm install -g yarn
