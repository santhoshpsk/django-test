from django.http import HttpResponse
import os


def index(request):
    return HttpResponse("Instance name: ")