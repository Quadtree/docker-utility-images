FROM alpine
RUN apk update
RUN apk add git python bash
RUN adduser -D cmp
RUN su -s /bin/bash -c 'cd ~ && git clone https://github.com/juj/emsdk.git' cmp
RUN su -s /bin/bash -c '~/emsdk/emsdk install latest' cmp
RUN su -s /bin/bash -c '~/emsdk/emsdk activate latest' cmp
ENTRYPOINT ["su", "-s", "/bin/bash", "cmp"]