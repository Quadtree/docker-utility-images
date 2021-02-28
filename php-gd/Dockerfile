FROM ubuntu:20.04
RUN DEBIAN_FRONTEND=noninteractive apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y php-cli php-gd
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y imagemagick
COPY policy.xml /etc/ImageMagick-6/policy.xml