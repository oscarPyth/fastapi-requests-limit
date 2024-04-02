from fastapi_ratelimit.storages.memory import MemoryStorage
from fastapi_ratelimit.storages.redis import RedisStorage

storage_engines = {"redis": RedisStorage, "memory": MemoryStorage}


def get_engines_availables():
    return storage_engines.keys()
