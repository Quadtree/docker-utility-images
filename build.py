#!/usr/bin/env python3

import os
import requests
import re
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--only')

args = parser.parse_args()

cur_path = os.path.realpath(os.path.dirname(__file__))

for fn in os.listdir(cur_path):
    if not args.only or fn == args.only:
        if os.path.isfile(os.path.join(cur_path, fn, 'Dockerfile')):
            tag = 'latest'

            with open(os.path.join(cur_path, fn, 'Dockerfile')) as f:
                for l in f:
                    m = re.match(r'FROM (([A-Za-z0-9_.-]+)/)?([A-Za-z0-9_.-]+)(:([A-Za-z0-9_.-]*))?', l)

                    if m:
                        tag = m.group(5)

            if tag and tag != 'latest':
                subprocess.run(['docker', 'build', '-t', 'quadtree2/' + fn + ':' + tag, fn])
                subprocess.run(['docker', 'push', 'quadtree2/' + fn + ':' + tag, fn])

            subprocess.run(['docker', 'build', '-t', 'quadtree2/' + fn + ':' + 'latest', fn])
            subprocess.run(['docker', 'push', 'quadtree2/' + fn + ':' + 'latest', fn])