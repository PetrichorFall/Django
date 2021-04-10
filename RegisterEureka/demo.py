import unittest

from py_eureka_client import logger
from py_eureka_client.eureka_client import EurekaServerConf, EurekaClient

logger.set_level("DEBUG")


class TestEurekaServer(unittest.TestCase):

    def test_init_eureka_server(self):
        es = EurekaServerConf(eureka_server="http://192.168.1.1:8761/eureka",
                              eureka_basic_auth_user="Django", eureka_basic_auth_password="123456", zone="zone1")
        print(es.servers)

        client = EurekaClient(eureka_server="http://192.168.1.1:8761/eureka", app_name="Django", instance_port=8000)
        client.start()
        # res = client.do_service("OTHER-SERVICE-NAME", "/service/context/path")
        # print("result of other service" + res)

        # when server is shutted down:
        # client.stop();
