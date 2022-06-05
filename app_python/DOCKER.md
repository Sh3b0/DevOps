# Best Practices

## In Production

- Used the lightweight `python:alpine` image.
- Used `.dockerignore` to ignore unnecessary files and folders (e.g., `Dockerfile`, `venv/`, `__pycache__`).
- Set environment variable `PYTHONUNBUFFERED` to a non-zero value to flush output and see container output in real-time.
- Used `--no-cache-dir` flag with `pip install` to prevent caching downloaded packages and make image size smaller.
