from django.utils.deprecation import MiddlewareMixin
from django_redis import get_redis_connection


class Listen(MiddlewareMixin):
    print("================")
    r = get_redis_connection("default")  # Use the name you have defined for Redis in settings.CACHES
    connection_pool = r.connection_pool
    print("Created connections so far: %d" % connection_pool._created_connections)
