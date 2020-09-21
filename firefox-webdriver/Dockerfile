# AUTO ^[\d.]+$
FROM selenium/standalone-firefox:80.0
USER root
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y python3-pip
USER seluser
RUN pip3 install selenium
ENTRYPOINT ["/bin/bash"]
