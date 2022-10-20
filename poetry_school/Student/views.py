import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
# Create your views here.


def index(request):
    data = []
    with open("./Student/data.json", "r") as file:
        data = json.loads(file.read())
    
    if request.method == "GET":
        return JsonResponse(data, safe = False)

    elif request.method == "POST":
        data.append(json.loads(request.body))
        with open("./Student/data.json", "w") as file:
            file.write(json.dumps(data))
        return JsonResponse(data, safe = False)

    elif request.method == "PUT":
        target = json.loads(request.body)
        for i in range(0,len(data)):
            if data[i]["id"] == target["id"]:
                data[i] = target
                break
        with open("./Student/data.json", "w") as file:
            file.write(json.dumps(data))
        return JsonResponse(data, safe = False)

    elif request.method == "DELETE":
        target = json.loads(request.body)
        for i in range(0,len(data)):
            if data[i]["id"] == target["id"]:
                del data[i]
                break
        with open("./Student/data.json", "w") as file:
            file.write(json.dumps(data))
        return JsonResponse(data, safe = False)

    