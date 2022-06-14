# Building Phase

## Goal

- Produce artifacts (e.g., executable, application image, software package, zipped source code, etc.) and version them.

- In this context, artifact is the **docker image** of the web application created from the corresponding `Dockerfile` for both apps.

## Steps

- Write a `Dockerfile`  in the root directory for each project.
- Add build and release instructions to the README.

## Best Practices

### General

- **Use a Dockerfile linter** (e.g., [hadolint](https://github.com/hadolint/hadolint)) as it helps build best practice Docker images.
- **Use a small base image** that does the job (e.g., alpine-based images) as it will make deployment faster while not taking much space.
- **Copy only the necessary files to the image** to make it smaller and faster, use `.dockerignore` to ignore unnecessary files and directories.
- **Use `EXPOSE` documentation** to make port-forwarding easier for other programmers reading your `Dockerfile`.
- **Push the image to a container registry** like DockerHub or the cloud-dedicated container registry for version control of app images and convenient deployment to the cloud.
- **Tag the images** with it’s version or corresponding the commit id from git to easily understand which version of the code is currently in the registry.

### Python App

- Set environment variable `PYTHONUNBUFFERED` to a non-zero value to see container output from host in real-time.
- Use `--no-cache-dir` flag with `pip install` to prevent caching downloaded packages and make image size smaller.

### NodeJS App

- Set environment variable `NODE_ENV` to `production` to configure ExpressJS with production settings.
- Use `npm ci` instead of `npm install` ([see why](https://docs.npmjs.com/cli/v8/commands/npm-ci)).

