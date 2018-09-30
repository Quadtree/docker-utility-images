#!/bin/bash

docker build -t emcc emcc/
docker build -t xvfb xvfb/
docker build -t firefox-webdriver firefox-webdriver/