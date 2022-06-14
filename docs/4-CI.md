# Continuous Integration

## Table of Contents

1. [Overview](#1.-Overview)

   1.1. [GitHub Actions](#1.1.-GitHub-Actions)

   1.2. [Jenkins](#1.2.-Jenkins)

2. [Goal](#2.-Goal)

3. [Steps](#3.-Steps)

   3.1. [Python App](#3.1.-Python-App)

   3.2. [NodeJS App](#3.2.-NodeJS-App)

4. [Best Practices](#4.-Best-Practices)

   4.1. [GitHub Actions](#4.1-GitHub-Actions)

   4.2. [Jenkins](#4.2.-Jenkins)

## 1. Overview

### 1.1. GitHub Actions

- A **workflow** (described as a YAML file) defines **jobs** that are triggered by some events (e.g., pushing to the remote repository).
- A job is described by a sequence of **steps** and **runs on** dedicated GitHub **runner** (**windows**/**ubuntu**/**macOS**).
- Jobs run in parallel unless they **need** other jobs as dependencies.
- A job can **run** scripts, **use** 3rd-party actions written by GitHub actions team or the community ([marketplace](https://github.com/marketplace?type=actions)).

### 1.2. Jenkins

- A `Jenkinsfile` (typically declarative but can also use groovy script) is used to create a Jenkins **pipeline** which consists of **stages** (e.g., build, test and deploy).
- Each stage runs a sequence of **steps**, stages can be configured to run in **parallel** and a **post** stage can be configured to run after certain stages or steps are done (**always**, on **success**, or **failure**).
- Jenkins can utilize default or custom **environment** variables, can integrate with git repositories, can run stages conditionally based on **parameters** and **expressions**, and has several **plugins** for extending its functionality and integration with other tools.
- Jenkins server can be deployed as a container that exposes a web UI for configuration and checking build status.

## 2. Goal

- **Set up Continuous Integration** to automatically **test**, **build**, and **release**  both applications as new code gets pushed to the main branch.

## 3. Steps

### 3.1. Python App

- Create a workflow file in [`/.github/workflows/`](/.github/workflows/) and make sure it runs only when there are relevant updates (by adding `on` triggers).
- Add steps for installing requirements using `pip` and running `pytest`.
- Use docker build and push actions to create a new version of the application image, login to DockerHub, then push the image with a new tag.
- Cache `pip` downloaded packages to make CI run faster.
- [Cache docker image layers.](https://github.com/docker/build-push-action/blob/master/docs/advanced/cache.md)

### 3.2. NodeJS App

- Navigate to `app_nodejs/jenkins` and run `docker-compose up` to run the Jenkins server.
- Use the password from the command line to access the UI at http://localhost:8080
- Set up and configure the necessary plugins for credentials, git, nodejs, and docker.
- Write `Jenkinsfile` to install dependencies, run server, run tests, then login and push image to DockerHub.
- Configure Jenkins to find `Jenkinsfile` by path and run workflow on pushes to the `main` branch with included region set to `app_nodejs` directory.
- To trigger builds automatically, a webhook should be used.
  - For local Jenkins deployment this is not possible and we have to manually tell Jenkins to `Build now`
  - Or configure SCM polling (not recommended).

## 4. Best Practices

### 4.1. GitHub Actions

- Use an IDE plugin for help with syntax highlighting and linting of YAML files ([YAML by Redhat](ttps://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml) for VSCode).
- Keep actions minimal and don’t install unnecessary dependencies.
- Use GitHub secrets when working with credentials or tokens.
- Use [GitHub actions’ default environment variables](https://docs.github.com/en/actions/learn-github-actions/environment-variables#default-environment-variables) when working with the **runner** file system.
- With DockerHub, it’s more secure to use a generated-token with only the necessary permissions instead of using the password.
- Optimize workflow running time by [caching dependencies](https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows).

### 4.2. Jenkins

- **Use an IDE plugin** for help with syntax highlighting and linting of `Jenkinsfile`.
- **When running Jenkins as a docker container**
  - Use the official and maintained image for Jenkins.
    - [Official Image](https://hub.docker.com/r/jenkins/jenkins) at the time of writing this.
    - Alpine-based images introduce issues with the NodeJS plugin at the time of writing this.
  - Use docker files for Jenkins deployment instead of running a long, undocumented command in the terminal.
  - Pay attention to the base OS and the user under which the container is running since:
    - Using `sh` in `Jenkinsfile` runs commands under that user and that base OS.
    - Running docker commands (e.g., `docker push`) from Jenkinsfile can be problematic when Jenkins itself is running as a docker container, there are multiple [solutions](https://blog.container-solutions.com/running-docker-in-jenkins-in-docker) for this.

- **Use maintained plugins instead of shell scripts for:**
  - Setting up tools, environment and dependencies (it makes build faster and more portable).
  - Working with credentials for Jenkins and 3rd party integrations (it’s more secure and organized).

- **In production environments:**
  - Create users and configure access controls for them, not everyone should have access to the admin credentials.
  - Set up distributed builds as building on the built-in node can be a security issue.
