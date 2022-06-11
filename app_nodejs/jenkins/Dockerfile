FROM jenkins/jenkins:lts-jdk11

USER root
RUN apt-get update \
      && apt-get install --no-install-recommends -y sudo procps\
      && rm -rf /var/lib/apt/lists/*
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers
 
USER jenkins
