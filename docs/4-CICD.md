# Continuous Integration

> It’s about setting up an automated process for incorporating new code into existing infrastructure.

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
- When running Jenkins as a docker container, note the base OS and the user under which the container is running since:
  - Using `sh` in `Jenkinsfile` runs commands under that user and that base OS.
  - Alpine image can introduce issues with some plug-ins.

- **In production environments:**
  - Create users and configure access controls for them, not everyone should have access to the admin credentials.
  - Set up distributed builds as building on the built-in node can be a security issue.
- Use official credentials plugin to work with credentials for Jenkins and 3rd party integrations.
