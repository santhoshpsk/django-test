from django.http import HttpResponse
import os


def index(request):
    instance_name = os.getenv("instance_name")
    if "hit_num" not in os.environ:
        os.environ["hit_num"] = "1"
    hit_num = os.getenv("hit_num")
    os.environ["hit_num"] = str(int(hit_num) + 1)
    return HttpResponse("Instance name: " + instance_name + "<br>Hit Number: " + hit_num)