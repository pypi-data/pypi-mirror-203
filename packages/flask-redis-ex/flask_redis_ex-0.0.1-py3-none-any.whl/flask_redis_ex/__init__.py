from flask import current_app
from werkzeug.local import LocalProxy

import redis

def _get_client():
    if not hasattr(current_app, 'redisClient') or current_app.redisClient is None:
        config = current_app.config
        redis_url = config.get("REDIS_URL")
        current_app.redisClient = redis.from_url(redis_url)
    return getattr(current_app, 'redisClient', None)

redisClient: redis.Redis = LocalProxy(_get_client)