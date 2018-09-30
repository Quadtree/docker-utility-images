docker run -v /var/www/sbcrs1-calc-dev:/usr/local/sbcrs1:ro -it xvfb

export PATH="$PATH:/home/cmp/node_modules/.bin"

npm i protractor