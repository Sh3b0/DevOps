# Time App

- Sample app that shows current time for DevOps training.

## Used technology

- HTML, CSS, JS.
- Python (packages: Flask, Gunicorn).
- Docker (images: alpine, nginx).

## Development

`python` and `pip` are used, make sure you have them installed and available in `$PATH` then execute the following:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py # Or `flask run`
```

## Testing

```bash
python -m pytest
```

## Building and Pushing Image

```bash
# To build app image
docker build -t <USERNAME>/app_python .

# Testing the built image locally (http://localhost:8080)
docker run -p8080:8080 app_python

# Pushing a new version to dockerhub
docker login -u <USERNAME> # Enter password/token when prompted
tagname=$(git log -1 --pretty=format:%h) # Or use semantic versioning
docker tag <USERNAME>/app_python <USERNAME>/app_python:$tagname
docker push <USERNAME>/app_python --all-tags
```

