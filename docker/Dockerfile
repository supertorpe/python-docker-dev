#FROM python:3.11.10-slim
#FROM python:3.12.7-slim
FROM python:3.13.0-slim

ENV RUFF_CACHE_DIR=/tmp/.ruff_cache
ENV MYPY_CACHE_DIR=/tmp/.mypy_cache

RUN echo "deb http://ftp.es.debian.org/debian/ stable main" > /etc/apt/sources.list.d/debian.list && \
    apt update &&\
    apt -y upgrade &&\
    rm -rf /var/lib/apt/lists/*

RUN python3 -m venv /opt/venv && \
    /opt/venv/bin/pip install --upgrade pip &&\
    chmod -R 777 /opt/venv

COPY ./app/requirements.txt /tmp/requirements.txt
RUN /opt/venv/bin/pip install -r /tmp/requirements.txt &&\
    rm /tmp/requirements.txt

COPY ./docker/startup.sh /

WORKDIR /app

ENTRYPOINT ["/startup.sh"]