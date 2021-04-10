import py_eureka_client.eureka_client as eureka_client
from django.utils.deprecation import MiddlewareMixin

server_host = "127.0.0.1"
server_port = 8001


def _register_():
    client = eureka_client.EurekaClient(eureka_server="http://127.0.0.1:8761/eureka", app_name="Django",
                                        instance_host=server_host, instance_port=server_port,
                                        ha_strategy=eureka_client.HA_STRATEGY_RANDOM)
    client.start()


def execute_register():
    client_init = eureka_client.init(eureka_server="http://127.0.0.1:8761/eureka", app_name="Django",
                                     instance_host=server_host, instance_port=server_port,
                                     ha_strategy=eureka_client.HA_STRATEGY_RANDOM)


class Eureka(MiddlewareMixin):
    print("========start to register eureka=======")
    execute_register()
    # def __init__(self, port):
    #     super().__init__()
    #     self.port = port
    #     execute_register()

    # @staticmethod
    # def execute_register():
    #     client_init = eureka_client.init(eureka_server="http://127.0.0.1:8761/eureka", app_name="Django",
    #                                      instance_host=server_host, instance_port=server_port,
    #                                      ha_strategy=eureka_client.HA_STRATEGY_RANDOM)

