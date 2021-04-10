import json

from django.http import HttpResponse as resp, HttpResponse
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from django_redis import get_redis_connection


@csrf_exempt  # post 请求会被csrf拦截，403，需要放行
def _test(req):
    if req.method == 'GET':
        print("=================get 请求============")
        get = req.GET.get('id')
        print("========the request parameters is :", get)
        return resp('Hello python world')
    elif req.method == 'POST':
        print("=================post 请求============== ")
        json_loads = json.loads(req.body, encoding='utf-8')
        print(json_loads)
        # 返回的时候必须将字典序列化成字符串 用json.dumps,  这个是返回给前端一个json对象
        return resp(json.dumps({'key': '我是返回结果'}), content_type='application/json;charset=utf-8')


def get_name(request):
    conn = get_redis_connection()
    name = conn.get('name').decode('utf-8')
    return HttpResponse(name)


@cache_page(5)
def test(request):
    import time
    ctime = time.time()
    return HttpResponse(str(ctime))
