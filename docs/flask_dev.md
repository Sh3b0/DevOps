# During development

- Use **Flask debugging server**, this will:
  - Log all requests in terminal and reload server on code changes.
  - Allow accessing debug info from the app when errors occur.
- Work in a **virtual environment**
  - Write dependencies with their versions in `requirements.txt` for the `venv` to be reproducible by other programmers who will work on the project.
  - Using a `venv` also isolates the project and avoids polluting your OS file system with unnecessary packages that will take space and make indexing slower and may result in dependency conflicts.
- **Follow PEP8 style guide** and enforce it with tools and extensions
  - For example: configure `autopep8` to run on save in the IDE.
- **Follow recommended directory structure and directory/file naming**
  - For Flask apps: use `templates` directory for HTML templates and `static` directory for static files with subdirectories for `css`, `js`, `images`, and any other needed static files.

- To connect Python webapps to the webserver, we need a **Web Server Gateway Interface (WSGI)** like `gunicorn`.
