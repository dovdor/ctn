FROM python:3.7.0-alpine

ADD build/requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt

ADD src /app
WORKDIR /app

ENTRYPOINT [ "/app/ctn.py" ]
