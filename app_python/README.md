# Time App

- Sample app that shows current time for DevOps training.
- Check [PYTHON.md](./PYTHON.md) and [DOCKER.md](./DOCKER.md) for best practices used in development and production respectively. 

## Used technology

- HTML, CSS, JS.
- Python (packages: Flask, Gunicorn).
- Docker (images: alpine, nginx).
- docker-compose

## Development in Linux

`python` and `pip` are used, make sure you have them installed and available in `$PATH` then execute the following inside `app` directory.

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Production

```bash
cd app
docker build -t time_app .
docker run -p8080:8080 time_app
```

## Pushing to DockerHub

```
tagname=$(git log -1 --pretty=format:%h)
docker tag time_app sh3b0/time_app:tagname
docker tag time_app sh3b0/time_app:latest
docker push sh3b0/time_app:tagname
```

