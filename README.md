# Building
* ./build.sh

If the build fails with weird errors from apt-get, the problem is probably that the cache is out of date. Run the offending build with `--no-cache` before the `-t`.

# Image Running Commands

## emcc
* docker run -v /var/www/tmp/znt_web:/usr/local/znt_web -v /var/data/zoomable-note-taker:/usr/local/znt_src:ro -it emcc
* /usr/local/znt_src/emcc_build.sh --debug

## chrome-webdriver
* docker run -v /var/data/zoomable-note-taker:/usr/local/znt_src:ro -it chrome-webdriver
* python3 /usr/local/znt_src/tests/run.py