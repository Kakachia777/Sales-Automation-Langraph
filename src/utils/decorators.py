from functools import wraps
from cachetools import TTLCache
import time

def rate_limit(calls: int, period: int = 60):
    """Rate limiting decorator"""
    cache = TTLCache(maxsize=100, ttl=period)
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_time = time.time()
            cache_key = f"{func.__name__}:{current_time // period}"
            
            if cache_key in cache:
                if cache[cache_key] >= calls:
                    sleep_time = period - (current_time % period)
                    time.sleep(sleep_time)
                    cache.clear()
            else:
                cache[cache_key] = 0
            
            cache[cache_key] += 1
            return func(*args, **kwargs)
        return wrapper
    return decorator

def cache_response(ttl: int = 3600):
    """Caching decorator with TTL"""
    cache = TTLCache(maxsize=100, ttl=ttl)
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = str(args) + str(kwargs)
            if key in cache:
                return cache[key]
            result = func(*args, **kwargs)
            cache[key] = result
            return result
        return wrapper
    return decorator 