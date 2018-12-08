FROM ubuntu:18.04
RUN apt-get update && apt-get install -y python3-pip npm nodejs-legacy chromium
RUN npm install -g protractor@4.0.5 webdriver-manager@10.2.3
RUN webdriver-manager update
RUN useradd seluser
USER seluser
ENTRYPOINT ["/bin/bash"]