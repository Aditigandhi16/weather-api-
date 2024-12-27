import redis
import os

redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = os.getenv("REDIS_PORT", 6379)
cache_client = redis.StrictRedis(
    host=redis_host, port=redis_port, decode_responses=True)

def get(key):
    return cache_client.get(key)

def set(key, value, expiration=600):
    cache_client.set(key, value, ex=expiration)
