# Development

## Table of Contents

1. [Goal](#1-Goal)

2. [Steps](#2-Steps)

   2.1. [Python App](#21-Python-App)

   2.2. [NodeJS App](#22-NodeJS-App)

3. [Best Practices](#3-Best-Practices)

   3.1. [Python App](#31-Python-App)

   3.2. [NodeJS App](#32-NodeJS-App)

## 1. Goal

- Create two sample applications using different technologies to apply DevOps practices on them.

## 2. Steps

### 2.1 Python App

- Create `app_python` directory and initialize a virtual environment with `python -m venv venv`
- Install required project dependencies with `pip install` then freeze the environment with `pip freeze > requirements.txt`
- Implement application logic.
- Create a README with description and instructions for local development.

### 2.2 NodeJS App

- Create `app_nodejs` directory and initialize the project with `npm init`  
- Install project dependencies and dev dependencies with `npm install`.
- Implement application logic.
- Create a README with description and instructions for local development.

## 3. Best practices

### 3.1. Python App

- Use **Flask debugging server**, this will:
  - Log all requests in terminal and reload server on code changes.
  - Allow accessing debug info from the app when errors occur.
- Work in a **virtual environment**
  - Write dependencies with their versions in `requirements.txt` for the `venv` to be reproducible by other programmers who will work on the project.
  - Using a `venv` also isolates the project and avoids polluting your OS file system with unnecessary packages that will take space and make indexing slower and may result in dependency conflicts.
- **Follow PEP8 style guide** and enforce it with tools and extensions
  - For example: configure `autopep8` to run on save in the IDE.
- **Follow recommended directory structure and directory/file naming. Example:**
  - Use `templates` directory for HTML templates and `static` directory for static files with subdirectories for `css`, `js`, `images`, and any other needed static files.
- To connect Python webapps to the webserver, we need a **Web Server Gateway Interface (WSGI)** like `gunicorn`.

### 3.2. NodeJS App

- **Use development server** (e.g., `webpack-dev-server` for frontend and node with `nodemon` for backend) to get useful logs in terminal and reload server on code changes.
- **Use devDependencies** for dependencies that are not required in production (they won’t get installed when NODE_ENV is set to production).
- **Use TypeScript** to write more reliable and type-safe code.
- **Use ESLint with** recommended typescript rules.
- **Follow a common directory structure and directory/file naming. Example:**
  - Use `src` directory for source code
  - `public` or `static` directory for static files with subdirectories for `css`, `js`, `images`, and any other needed static files.
  - `dist` directory for frontend bundles (and maybe for `js` files compiled with `tsc`).
