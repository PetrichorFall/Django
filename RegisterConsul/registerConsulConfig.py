import consul
from django.utils.deprecation import MiddlewareMixin

CONSUL_IP = "127.0.0.1"
CONSUL_PORT = 8500
APP_NAME = "Django"
TAGS = ["group=Django","version=1.0"]


def _register_(applicationName, host, port, tags):
    consul_client = consul.Consul(host, port)
    consul_client.agent.service.register(
        applicationName,
        applicationName,
        host,
        port,
        tags,
        check=consul.Check.tcp(host, port, "5s", "30s", "30s")
    )
    return consul_client


class Consul(MiddlewareMixin):
    print("========= start to register consul========")
    client = _register_(APP_NAME, CONSUL_IP, CONSUL_PORT, TAGS)
    services = client.agent.services()
    service = services.get(APP_NAME)
    if not service:
        print("******** not register **********")
    addr = "{0}:{1}".format(service['Address'], service['Port'])
    print("the address is =========", addr)


    # def __init__(self, port):
    #     print("========= start to register consul========")
    #     self.port = port
    #     client = _register_(APP_NAME, CONSUL_IP, CONSUL_PORT, TAGS)
    #     services = client.agent.services()
    #     service = services.get(APP_NAME)
    #     if not service:
    #         print("******** not register **********")
    #     addr = "{0}:{1}".format(service['Address'], service['Port'])
    #     print("the address is =========", addr)

    # @staticmethod
    # def _register_(applicationName, host, port, tags):
    #     consul_client = consul.Consul(host, port)
    #     consul_client.agent.service.register(
    #         applicationName,
    #         applicationName,
    #         host,
    #         port,
    #         tags,
    #         check=consul.Check.tcp(host, port, "5s", "30s", "30s")
    #     )
    #     return consul_client