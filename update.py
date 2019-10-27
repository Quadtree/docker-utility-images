#!/usr/bin/env python3

# https://registry.hub.docker.com/v2/repositories/selenium/standalone-chrome/tags/
# https://registry.hub.docker.com/v1/repositories/library/node/tags

import os
import requests
import re

cur_path = os.path.realpath(os.path.dirname(__file__))

for fn in os.listdir(cur_path):
    try:
        dockerfile_lines = []

        with open(os.path.join(cur_path, fn, 'Dockerfile')) as f:
            for l in f:
                dockerfile_lines.append(l.strip())

        base_image_repository = None
        base_image = None
        base_image_tag = None

        for l in dockerfile_lines:
            m = re.match(r'FROM (([A-Za-z0-9_-]+)/)?([A-Za-z0-9_-]+)(:([A-Za-z0-9_-]*))?', l)

            if m:
                base_image_repository = m.group(2)
                base_image = m.group(3)
                base_image_tag = m.group(5)

        print('base_image_repository=' + str(base_image_repository))
        print('base_image=' + str(base_image))
        print('base_image_tag=' + str(base_image_tag))


    except NotADirectoryError: pass
    except FileNotFoundError: pass