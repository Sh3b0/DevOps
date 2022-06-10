# Continuous Integration

> It’s about setting up an automated process for incorporating new code into existing infrastructure

## GitHub Actions

Setting up CI with Github Actions for the Python app.

### Overview

- A **workflow** (described as a YAML file) defines **jobs** that are triggered by some events (e.g., pushing to the remote repository).
- A job is described by a sequence of **steps** and **runs on** dedicated GitHub **runner** (**windows**/**ubuntu**/**macOS**).
- Jobs run in parallel unless they **need** other jobs as dependencies.
- A job can **run** scripts, **use** 3rd-party actions written by GitHub actions team or the community ([marketplace](https://github.com/marketplace?type=actions)).

### Practice

- Add workflows in [`/.github/workflows/`](/.github/workflows/) and make sure they run only when there are relevant updates (by adding `on` triggers).
- Use an IDE plugin for help with syntax highlighting and linting of YAML files.
  - **For VSCode:** [YAML by Redhat](ttps://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml)

- Keep actions minimal and don’t install unnecessary dependencies.
- Use GitHub secrets when working with credentials or tokens.
- Use [GitHub actions’ default environment variables](https://docs.github.com/en/actions/learn-github-actions/environment-variables#default-environment-variables) when working with the **runner** file system.
- With DockerHub, it’s more secure to use a generated-token with only the necessary permissions instead of using the password.
- Optimize workflow running time by [caching dependencies](https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows).
  - Cache `pip` downloaded packages.
  - [Cache docker image layers.](https://github.com/docker/build-push-action/blob/master/docs/advanced/cache.md)

## Jenkins

Setting up CI with Jenkins for the NodeJS app.

### Overview

- A `Jenkinsfile` (typically declarative but can also use groovy script) is used to create a Jenkins **pipeline** which consists of **stages** (e.g., build, test and deploy).
- Each stage runs a sequence of **steps**, stages can be configured to run in **parallel** and a **post** stage can be configured to run after certain stages or steps are done (**always**, on **success**, or **failure**).
- Jenkins can utilize default or custom **environment** variables, can integrate with git repositories, can run stages conditionally based on **parameters** and **expressions**, and has several **plugins** for extending it’s functionality and integration with other tools.

### Practice

- Jenkins server can be deployed as a container that exposes a web UI for configuration and checking build status.

- [BlueOcean](https://www.jenkins.io/projects/blueocean/) is a plugin built on top of Jenkins that provides a better UI/UX for Jenkins and can automatically create `Jenkinsfile` 

  - Running BlueOcean as a docker container with port forwarding and a volume for persisting data.

    ```bash
    docker run --name jenkins -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkinsci/blueocean:1.25.5
    ```

  - Access the UI at http://localhost:8080, use default credentials `admin` and the password from the previous command output, you can also create a different user account or add plug-ins.
  - Configure credentials for GitHub both in BlueOcean and Jenkins.

- 
