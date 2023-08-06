from flask import current_app
from werkzeug.local import LocalProxy

import redis

def _get_client():
    if not hasattr(current_app, 'redis_client') or current_app.redis_client is None:
        config = current_app.config
        redis_url = config.get("REDIS_URL")
        current_app.redis_client = redis.from_url(redis_url)
    return getattr(current_app, 'redis_client', None)

redis_client: redis.Redis = LocalProxy(_get_client)