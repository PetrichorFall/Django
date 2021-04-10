
from redis import StrictRedis
from rest_framework.response import Response
from rest_framework.views import APIView
from DjangoMicroServices.util import code
from DjangoMicroServices.views.test_framework_rest import logger


class RedisDemo(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("$$$$$$$$$$test redis demo@@@@@@@@@@")

    def get(self, request, *args, **kwargs):
        logger.info('========get请求==============')
        sr = StrictRedis(host='192.168.1.128', port=6379, db=0, max_connections=10)
        sr.set("aaa", "bbb")
        return Response({code.CODE_KEY: code.SUCCESS_CODE, 'data': '我是返回结果'})
