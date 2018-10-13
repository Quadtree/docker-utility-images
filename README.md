Helpful commands for running images:

* docker run -v /var/www/tmp/znt_web:/usr/local/znt_web -v /var/data/zoomable-note-taker:/usr/local/znt_src:ro -it emcc
* /usr/local/znt_src/emcc_build.sh --debug


* docker run -v /var/data/zoomable-note-taker:/usr/local/znt_src:ro -it chrome-webdriver
* python3 /usr/local/znt_src/tests/run.py