# Dockerized Flask Application with Redis

This project demonstrates how to containerize a simple Flask web application that connects to Redis and counts visits to the page using Docker and Docker Compose.

## Project Structure
```
docker-project/
│── app/
│   ├── app.py               # Flask application code
│   ├── requirements.txt      # Dependencies for Flask
│── Dockerfile                # Image definition for the Flask app
│── docker-compose.yml        # Docker Compose file
```

## Step 1: Create the Flask Application
Inside the `app/` folder, create `app.py` with the following content:

```python
from flask import Flask
import redis
import os

app = Flask(__name__)

# Connect to Redis
cache = redis.Redis(host=os.getenv('REDIS_HOST', 'redis'), port=6379)

@app.route('/')
def hello():
    count = cache.incr('visits')
    return f'Hello, World! You have visited {count} times.'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
```

## Step 2: Add Dependencies
In `app/`, create a `requirements.txt` file to specify the dependencies:
```
Flask
redis
```

## Step 3: Create the Dockerfile
At the root of your project, create a `Dockerfile` to define the Flask app's container image:

```dockerfile
# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy application files
COPY app/ /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
```

## Step 4: Create the Docker Compose File
Create a `docker-compose.yml` file to define the multi-container setup:

```yaml
version: '3'
services:
  web:
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - redis
    environment:
      - REDIS_HOST=redis
  redis:
    image: "redis:alpine"
    ports:
      - "6379:6379"
```

## Step 5: Build and Run the Application
In the root directory, run the following command to build the images and start the containers:

```sh
docker-compose up --build
```

## Step 6: Access the Web Application
Open your web browser and visit:

```
http://localhost:5000
```

You should see output similar to:
```
Hello, World!
You have visited 1 times.
```

## Conclusion
This project provides a simple example of using Docker to containerize a Flask application with Redis. You can extend this by adding more features, logging, and persistence for Redis.

Happy coding! 🚀
