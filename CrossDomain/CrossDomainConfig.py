from django.utils.deprecation import MiddlewareMixin
from django import http

XS_SHARING_ALLOWED_ORIGINS = '*'
XS_SHARING_ALLOWED_METHODS = ['POST', 'GET', 'OPTIONS', 'PUT', 'DELETE']
# XS_SHARING_ALLOWED_METHODS = ['POST', 'GET']
XS_SHARING_ALLOWED_HEADERS = ['Content-Type', '*', 'token', 'Token']
XS_SHARING_ALLOWED_CREDENTIALS = 'true'

"""跨域解决方法二"""


class XsSharing(MiddlewareMixin):
    """
    This middleware allows cross-domain XHR using the html5 postMessage API.

    Access-Control-Allow-Origin: http://foo.example
    Access-Control-Allow-Methods: POST, GET, OPTIONS, PUT, DELETE

    Based off https://gist.github.com/426829
    """

    @staticmethod
    def process_request(request):
        print("================")
        if request.methos == "OPTIONS" and 'HTTP_ACCESS_CONTROL_REQUEST_METHOD' in request.META:
            response = http.HttpResponse()
            response['Access-Control-Allow-Origin'] = XS_SHARING_ALLOWED_ORIGINS
            response['Access-Control-Allow-Methods'] = ",".join(XS_SHARING_ALLOWED_METHODS)
            response['Access-Control-Allow-Headers'] = ",".join(XS_SHARING_ALLOWED_HEADERS)
            response['Access-Control-Allow-Credentials'] = XS_SHARING_ALLOWED_CREDENTIALS
            return response  # 不继续后面
        return None

    @staticmethod
    def process_response(self, request, response):
        response['Access-Control-Allow-Origin'] = XS_SHARING_ALLOWED_ORIGINS
        response['Access-Control-Allow-Methods'] = ",".join(XS_SHARING_ALLOWED_METHODS)
        response['Access-Control-Allow-Headers'] = ",".join(XS_SHARING_ALLOWED_HEADERS)
        response['Access-Control-Allow-Credentials'] = XS_SHARING_ALLOWED_CREDENTIALS
        return response
