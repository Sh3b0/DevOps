FROM python:alpine
COPY . /app
COPY requirements.txt /app
WORKDIR /app
ENV PYTHONUNBUFFERED=1
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "wsgi"]
