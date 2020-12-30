FROM python:3.7-buster

LABEL maintainer="Peng Xiao <xiaoquwl@gmail.com>"

RUN apk add --no-cache gcc libressl-dev musl-dev libffi-dev openssh-client sshpass&& \
    pip install --no-cache-dir ansible==2.8.18 && \
    apk del gcc libressl-dev musl-dev libffi-dev

WORKDIR /app

VOLUME ["/app"]

CMD []