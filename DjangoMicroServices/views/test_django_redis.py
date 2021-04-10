from django_redis import get_redis_connection
from rest_framework.response import Response
from rest_framework.views import APIView
from DjangoMicroServices.util import code
from DjangoMicroServices.views.test_framework_rest import logger
from django.core.cache import cache


class RedisDemo(APIView):

    print("$$$$$$$$$$test django redis demo@@@@@@@@@@")

    def get(self, request, *args, **kwargs):
        logger.info('========get请求==============')
        connection = get_redis_connection()
        connection.set("name", "测试")
        cache.set("foo", "value", timeout=25)
        return Response({code.CODE_KEY: code.SUCCESS_CODE, 'data': '设置成功'})
