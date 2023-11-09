
from fastapi_ratelimit.storages.redis import RedisStorage
from fastapi_ratelimit.storages.memory import MemoryStorage


storage_engines = {
    "redis": RedisStorage(host='localhost', port=6379),
    "memory": MemoryStorage()
}


def get_engines_availables():
    return storage_engines.keys()
