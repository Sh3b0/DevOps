FROM jenkins/jenkins:lts-jdk11

ENV DOCKERVERSION=20.10.9

USER 0

RUN curl -fsSLO https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKERVERSION}.tgz \
    && tar xzvf docker-${DOCKERVERSION}.tgz --strip 1 -C /usr/local/bin docker/docker \
    && rm docker-${DOCKERVERSION}.tgz \
    && apt-get update \
    && apt-get install --no-install-recommends -y procps \
    && rm -rf /var/lib/apt/lists/*
