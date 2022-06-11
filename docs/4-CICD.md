# CI/CD

## Goal

- **Continuous Integration:** automatically **test, build, and release** both applications as new code gets pushed to the main branch.
  - **Test:**
    - **Python app:** install requirements using `pip` then run `pytest`,
    - **NodeJS app:** install dependencies using `npm` then run `jest`.
  - **Build:** use `docker build` to create a new version of the application image.
  - **Release:** use `docker push` to push the newly created image to DockerHub.
- **Continuous deployment:** can then be achieved by configuring the cloud provider to update the  application image used in production as the new image gets deployed to DockerHub.
  - This can be achieved by configuring a **webhook**.
  - It’s worth mentioning that different cloud providers provide **their own container registry** which automatically integrates with their tools.

- Use **Github Actions with the Python app** and **Jenkins with the NodeJS app**. 

## GitHub Actions

### Overview

- A **workflow** (described as a YAML file) defines **jobs** that are triggered by some events (e.g., pushing to the remote repository).
- A job is described by a sequence of **steps** and **runs on** dedicated GitHub **runner** (**windows**/**ubuntu**/**macOS**).
- Jobs run in parallel unless they **need** other jobs as dependencies.
- A job can **run** scripts, **use** 3rd-party actions written by GitHub actions team or the community ([marketplace](https://github.com/marketplace?type=actions)).

### Practice

- Add workflows in [`/.github/workflows/`](/.github/workflows/) and make sure they run only when there are relevant updates (by adding `on` triggers).
- Use an IDE plugin for help with syntax highlighting and linting of YAML files.
  - For VSCode: [YAML by Redhat](ttps://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml)

- Keep actions minimal and don’t install unnecessary dependencies.
- Use GitHub secrets when working with credentials or tokens.
- Use [GitHub actions’ default environment variables](https://docs.github.com/en/actions/learn-github-actions/environment-variables#default-environment-variables) when working with the **runner** file system.
- With DockerHub, it’s more secure to use a generated-token with only the necessary permissions instead of using the password.
- Optimize workflow running time by [caching dependencies](https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows).
  - Cache `pip` downloaded packages.
  - [Cache docker image layers.](https://github.com/docker/build-push-action/blob/master/docs/advanced/cache.md)

## Jenkins

### Overview

- A `Jenkinsfile` (typically declarative but can also use groovy script) is used to create a Jenkins **pipeline** which consists of **stages** (e.g., build, test and deploy).
- Each stage runs a sequence of **steps**, stages can be configured to run in **parallel** and a **post** stage can be configured to run after certain stages or steps are done (**always**, on **success**, or **failure**).
- Jenkins can utilize default or custom **environment** variables, can integrate with git repositories, can run stages conditionally based on **parameters** and **expressions**, and has several **plugins** for extending it’s functionality and integration with other tools.
- Jenkins server can be deployed as a container that exposes a web UI for configuration and checking build status.

### Practice

- **Running Jenkins as a docker container**

  - Use the official and maintained image for Jenkins ([jenkins/jenkins](https://hub.docker.com/r/jenkins/jenkins) by the time of writing this)
  - Use docker files for Jenkins deployment instead of running a long, undocumented command in the terminal.
    - To run Jenkins server used in this project, navigate to `app_nodejs/jenkins` and run `docker-compose up`
  - Pay attention to the base OS and the user under which the container is running since:
    - Using `sh` in `Jenkinsfile` runs commands under that user and that base OS.
    - Alpine images can introduce issues with some plug-ins.
  
- **Use an IDE plugin for help with syntax highlighting and linting of `Jenkinsfile`.**

  - There doesn’t seem to be an official one for VSCode at the time of writing this.
  
- **Use maintained plugins instead of shell scripts for:**

  - Setting up tools, environment and dependencies (it makes build faster and more portable).
  - Working with credentials for Jenkins and 3rd party integrations (it’s more secure and centralized).

- **In production environments:**

  - Create users and configure access controls for them, not everyone should have access to the admin credentials.
  - Set up distributed builds as building on the built-in node can be a security issue.

  
