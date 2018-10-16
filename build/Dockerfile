FROM python:3.7.0-alpine

ADD build/entrypoint.sh /entrypoint.sh

ADD src /app
WORKDIR /app

ENTRYPOINT [ "/bin/sh" ]
CMD [ "/entrypoint.sh" ]
