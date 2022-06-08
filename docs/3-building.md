# Building Phase

> It’s about producing artifacts (e.g., executable, application image, package, zipped source code, etc.) and versioning them.

In this context, artifact is the **docker image** of the web application created from the corresponding `Dockerfile` for both apps.

## Python App

- Use the lightweight alpine-based python images.
- Use `.dockerignore` to ignore unnecessary files and folders (e.g., `Dockerfile`, `venv/`, `__pycache__`/).
- Set environment variable `PYTHONUNBUFFERED` to a non-zero value to flush output and see container output in real-time.
- Use `--no-cache-dir` flag with `pip install` to prevent caching downloaded packages and make image size smaller.

## NodeJS App

- Use the lightweight alpine-based node images.
- Use `.dockerignore` to ignore unnecessary files and folders (e.g., `node_modules`, `Dockerfile`)
- Set environment variable `NODE_ENV` to `production` to configure ExpressJS with production settings.
- Use `npm ci` instead of `npm i` ([see why](https://docs.npmjs.com/cli/v8/commands/npm-ci)).

