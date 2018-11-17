#!/bin/bash

ls | grep -vP 'build.sh|README.md' | xargs -n1 -I{} docker build -t '{}' '{}/'
