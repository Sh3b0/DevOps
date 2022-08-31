FROM python:alpine
WORKDIR /app
COPY requirements.txt .
ENV PYTHONUNBUFFERED=1
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8080
RUN useradd -ms /bin/bash app
USER app
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "wsgi"]
