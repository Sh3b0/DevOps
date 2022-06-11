FROM jenkins/jenkins:lts-jdk11

USER root
RUN apt-get update \
    && apt-get install --no-install-recommends -y procps=2:3.3.17-7+b1 \
    && rm -rf /var/lib/apt/lists/*

USER jenkins
