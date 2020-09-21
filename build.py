#!/usr/bin/env python3

import os
import requests
import re
import subprocess
import argparse
import threading

parser = argparse.ArgumentParser()
parser.add_argument('--only')
parser.add_argument('--no-cache', action="store_true")

args = parser.parse_args()

cur_path = os.path.realpath(os.path.dirname(__file__))

def build_image(fn):
    tag = 'latest'

    try:
        with open(os.path.join(cur_path, fn, 'version')) as f:
            for l in f:
                tag = l.strip()
                break
    except Exception: pass

    additional = []
    if args.no_cache: additional += ["--no-cache"]

    if tag and tag != 'latest':
        subprocess.run(['docker', 'build', '--build-arg', f'VERSION={tag}', '-t', 'quadtree2/' + fn + ':' + tag, fn] + additional)
        subprocess.run(['docker', 'push', 'quadtree2/' + fn + ':' + tag])

threads = []

for fn in os.listdir(cur_path):
    if not args.only or fn == args.only:
        if os.path.isfile(os.path.join(cur_path, fn, 'Dockerfile')):
            new_thread = threading.Thread(target=lambda fn=fn: build_image(fn))
            new_thread.start()
            threads.append(new_thread)

for thread in threads:
    thread.join()


