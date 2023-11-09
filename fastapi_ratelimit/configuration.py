from .storage_engines import get_engines_availables
from .handle_errors import EngineException
from .storage_engines import storage_engines


class Limiter:
    _instancia = None
    storage = None
    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super(Limiter, cls).__new__(cls)
        cls._instancia.init(*args, **kwargs)
        return cls._instancia

    def init(self, host='localhost', port='0000', storage_engine='memory'):
        self.host = host
        self.port = port
        if storage_engine not in get_engines_availables():
            raise EngineException("engine error", f'not exits the engine {storage_engine} connection')
        self.storage_engine = storage_engine
        self.storage = storage_engines.get(storage_engine, 'memory')




