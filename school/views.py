import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import *
from .forms import StudentForm
from django.core import serializers


# Create your views here.
def index(request):
    return JsonResponse({'name': 'yas'})


class StudentView(View):
    def get(self, request):
        data = serializers.serialize('json', Student.objects.all())
        return JsonResponse(json.loads(data), safe=False)

    def post(self, request):
        data=json.loads(request.body)
        form = StudentForm(data)
        if form.is_valid():
            form.save()
            return JsonResponse(form.data)
        return JsonResponse(form.errors, status=422)

    def put(self, request):
        data=json.loads(request.body)
        form = StudentForm(data, instance=Student.objects.get(first_name = data['first_name']))
        if form.is_valid():
            form.save()
            return JsonResponse(form.data)
        return JsonResponse(form.errors, status=422)
    
    def delete(self, request):
        data = json.loads(request.body)
        Student.objects.filter(first_name = data['first_name']).delete()

        data = serializers.serialize('json', Student.objects.all())
        return JsonResponse(json.loads(data), safe= False)
