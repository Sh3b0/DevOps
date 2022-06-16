FROM jenkins/jenkins:lts-jdk11

COPY docker /usr/bin/docker
RUN apt-get update \
    && apt-get install --no-install-recommends -y procps \
    && rm -rf /var/lib/apt/lists/*