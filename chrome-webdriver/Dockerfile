FROM selenium/standalone-chrome
USER root
RUN apt-get update && apt-get install -y python3-pip
USER seluser
RUN pip3 install selenium
ENTRYPOINT ["/bin/bash"]