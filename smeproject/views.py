from django.http import HttpResponse
from django.http import HttpRequest
from . import controller
import json

def predict(request: HttpRequest):
    br = request.GET.get("d")
    bdata = json.loads(br)
    # print()
    # print(type(json.loads(br)))
    # bjson = json.load(br.decode('utf-8'))
    # print(bjson)
    # [[5,5,5,5,5,0,0,0,0,0,0,0,0,0]]
    # print(type(br))
    jibu = controller.predict(bdata)
    return HttpResponse(jibu)