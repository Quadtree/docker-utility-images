#!/bin/bash

docker build -t emcc emcc/
docker build -t xvfb xvfb/
docker build -t firefox-webdriver firefox-webdriver/
docker build -t chrome-webdriver chrome-webdriver/
docker build -t ubuntu-deploy ubuntu-deploy/
docker build -t node-iso node-iso/