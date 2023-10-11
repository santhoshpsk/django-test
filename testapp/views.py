from django.http import HttpResponse, HttpRequest
import os


def index(request: HttpRequest):
    return HttpResponse("Headers: " + str(request.headers))