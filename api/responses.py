from django.http import HttpResponse


class Http401(HttpResponse):
    status_code = 401
