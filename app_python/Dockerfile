FROM python:alpine
WORKDIR /home/app/app
COPY requirements.txt .
ENV PYTHONUNBUFFERED=1
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8080
RUN addgroup -S app && adduser -S app -G app
USER app
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "wsgi"]
