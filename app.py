from flask import Flask
import redis
import os

app = Flask(__name__)

# Connect to Redis
cache = redis.Redis(host=os.getenv('REDIS_HOST', 'redis'), port=6379)  # Fixed: Added missing )

@app.route('/')
def hello():
    count = cache.incr('visits')
    return f'Hello, World! You have visited {count} times.'  # Added space after comma

if __name__ == "__main__":  # Fixed: Replaced ; with :
    app.run(host='0.0.0.0')
