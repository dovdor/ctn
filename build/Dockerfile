FROM python:3.7.0-alpine

ADD build/requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt

ADD build/entrypoint.sh /entrypoint.sh

ADD src /app
WORKDIR /app

ENTRYPOINT [ "/bin/sh" ]
CMD [ "/entrypoint.sh" ]
