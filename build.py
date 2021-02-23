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

REPO = 'ghcr.io/quadtree'

def run_subproc(cmd):
    print(cmd)
    proc = subprocess.run(cmd, check=True, capture_output=True)
    print(proc.stdout.decode('utf8'))
    print(proc.stderr.decode('utf8'))

any_error = False
    
def build_image(fn):
    global any_error
    try:
        tag = 'latest'

        try:
            with open(os.path.join(cur_path, fn, 'version')) as f:
                for l in f:
                    tag = l.strip()
                    break
        except Exception: pass

        additional = []
        if args.no_cache: additional += ["--no-cache"]

        cmd1 = ['docker', 'build', '--build-arg', f'VERSION={tag}', '-t', f'{REPO}/' + fn + ':' + tag, fn] + additional
        run_subproc(cmd1)
        cmd2 = ['docker', 'push', f'{REPO}/' + fn + ':' + tag]
        run_subproc(cmd2)
    except Exception as ex:
        print(f"Building image {fn} failed with error: {ex}")
        any_error = True

threads = []

for fn in os.listdir(cur_path):
    if not args.only or fn == args.only:
        if os.path.isfile(os.path.join(cur_path, fn, 'Dockerfile')):
            new_thread = threading.Thread(target=lambda fn=fn: build_image(fn))
            new_thread.start()
            threads.append(new_thread)

for thread in threads:
    thread.join()

if any_error:
    raise Exception("Build failed with errors")

