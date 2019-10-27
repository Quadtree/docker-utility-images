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

        tag_regex = None

        for l in dockerfile_lines:
            m = re.match(r'FROM (([A-Za-z0-9_.-]+)/)?([A-Za-z0-9_.-]+)(:([A-Za-z0-9_.-]*))?', l)

            if m:
                base_image_repository = m.group(2)
                base_image = m.group(3)
                base_image_tag = m.group(5)

            m = re.match(r'# AUTO (.+)', l)

            if m:
                tag_regex = m.group(1)

        if not tag_regex: continue

        if not base_image_repository: base_image_repository = 'library'

        print('base_image_repository=' + str(base_image_repository))
        print('base_image=' + str(base_image))
        print('base_image_tag=' + str(base_image_tag))

        new_tag = None

        next_uri = 'https://registry.hub.docker.com/v2/repositories/' + base_image_repository + '/' + base_image + '/tags/'

        while not new_tag:
            print('Fetching ' + next_uri)
            resp = requests.get(next_uri)

            if 'next' in resp.json():
                next_uri = resp.json()['next']

            for result in resp.json()['results']:
                #if result['name'] != 'latest':
                if re.match(tag_regex, result['name']):
                    print(result['name'])
                    new_tag = result['name']
                    break

        if new_tag:
            with open(os.path.join(cur_path, fn, 'Dockerfile'), 'w') as f:
                for l in dockerfile_lines:
                    if 'FROM' in l:
                        if base_image_repository:
                            f.write('FROM ' + base_image_repository + '/' + base_image + ':' + new_tag + '\n')
                        else:
                            f.write('FROM ' + base_image + ':' + new_tag + '\n')
                    else:
                        f.write(l + '\n')


    except NotADirectoryError: pass
    except FileNotFoundError: pass