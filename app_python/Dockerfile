FROM python:alpine
WORKDIR /app
COPY requirements.txt .
ENV PYTHONUNBUFFERED=1
RUN pip install --no-cache-dir -r requirements.txt \ 
    && addgroup -S app && adduser -S app -G app
USER app
COPY . .
EXPOSE 8080
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "wsgi"]
