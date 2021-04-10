import json
import logging

from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView

from DjangoMicroServices.util import code

logger = logging.getLogger('log')


# @csrf_exempt

class Demo(APIView):
    print("$$$$$$$$$$rest_framework invoke demo@@@@@@@@@@")

    def post(self, request, *args, **kwargs):
        logger.info('========POST请求==============')
        request_body = json.loads(request.body, encoding='utf-8')
        print(request_body)
        return Response({code.CODE_KEY: code.SUCCESS_CODE, 'data': '我是返回结果'})
