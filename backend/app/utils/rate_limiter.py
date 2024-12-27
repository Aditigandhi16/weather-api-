from redis import StrictRedis
from fastapi import HTTPException
import time
from app.config import config

redis_client = StrictRedis(host="localhost", port=6379, decode_responses=True)

def rate_limiter(func):
    async def wrapper(*args, **kwargs):
        client_ip = kwargs.get("request").client.host
        current_time = time.time()

        key = f"rate_limit:{client_ip}"
        count = redis_client.get(key)

        if count and int(count) >= config.RATE_LIMIT:
            raise HTTPException(status_code=429, detail="Rate limit exceeded")

        pipeline = redis_client.pipeline()
        pipeline.incr(key)
        pipeline.expire(key, 60)
        pipeline.execute()

        return await func(*args, **kwargs)
    return wrapper
