from dependency_injector import containers, providers

# Definición de una clase de servicio simple
class Service:
    def __init__(self, value):
        self.value = value

    def do_something(self):
        return f"Service with value {self.value}"

# Creación del contenedor
class Container(containers.DeclarativeContainer):
    # Configuración que se puede inyectar desde variables de entorno u otro lado
    config = providers.Configuration()

    # Un proveedor que construye instancias de Service usando la configuración
    service_provider = providers.Factory(Service, value=config.values)

# Configuración del contenedor
container = Container()
container.config.values.override("We've injected this value!")

# Uso del proveedor para obtener una instancia del servicio
service_instance = container.service_provider()
print(service_instance.do_something())