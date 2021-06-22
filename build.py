#!/usr/bin/env python3

import os
from typing import IO, Optional
import requests
import re
import subprocess
import argparse
import threading

parser = argparse.ArgumentParser()
parser.add_argument('--only')
parser.add_argument('--no-cache', action="store_true")
parser.add_argument('--use-buildkit', type=int, default=1)

args = parser.parse_args()

cur_path = os.path.realpath(os.path.dirname(__file__))

REPO = 'ghcr.io/quadtree'

def watch_pipe(fn, txt, pipe:Optional[IO[bytes]]):
    for l in pipe:
        print(f'{fn} {txt}: {l.decode("utf8").strip()}')

def run_subproc(fn, cmd):
    print(cmd)
    env_vars = dict(os.environ)
    if args.use_buildkit:
        env_vars["DOCKER_BUILDKIT"] = "1"

    proc = subprocess.Popen(cmd, env=env_vars, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    stdout_thread = threading.Thread(target=lambda: watch_pipe(fn, 'stdout', proc.stdout))
    stdout_thread.start()
    stderr_thread = threading.Thread(target=lambda: watch_pipe(fn, 'stderr', proc.stderr))
    stderr_thread.start()
    stdout_thread.join()
    stderr_thread.join()
    proc.wait()
    if proc.returncode != 0:
        raise Exception(f"{fn} msg: {cmd} failed with code {proc.returncode}")

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

        full_name = f'{REPO}/' + fn + ':' + tag

        cmd1 = ['docker', 'build', '--build-arg', 'BUILDKIT_INLINE_CACHE=1', '--cache-from', full_name, '--build-arg', f'VERSION={tag}', '-t', full_name, fn] + additional
        run_subproc(fn, cmd1)
        cmd2 = ['docker', 'push', full_name]
        run_subproc(fn, cmd2)
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

