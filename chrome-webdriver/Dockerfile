# AUTO ^[\d.]+$
FROM selenium/standalone-chrome:85.0
USER root
RUN apt-get update && apt-get install -y python3-pip
USER seluser
RUN pip3 install selenium
ENTRYPOINT ["/bin/bash"]
