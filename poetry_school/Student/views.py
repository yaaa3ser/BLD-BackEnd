import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.views import View
from Student.models import Student
from django.core import serializers
# Create your views here.

class StudentView(View):
    def get (self, request):
        data = serializers.serialize('json', Student.objects.all())
        return JsonResponse(json.loads(data), safe= False)

    def post(self, request, *args, **kwargs):
        st = json.loads(request.body)
        Student.objects.create(
            first_name = st['first_name'], 
            last_name = st['last_name'],
            age = st['age'],
            email = st['email']
            )
        data = serializers.serialize('json', Student.objects.all())
        return JsonResponse(json.loads(data), safe= False)

    def put(self, request, *args, **kwargs):
        st = json.loads(request.body)
        Student.objects.filter(first_name = st['first_name']).update(
            first_name = st['first_name'], 
            last_name = st['last_name'],
            age = st['age'],
            email = st['email']
        )
        data = serializers.serialize('json', Student.objects.all())
        return JsonResponse(json.loads(data), safe= False)

    
    def delete(self, request, *args, **kwargs):
        st = json.loads(request.body)
        Student.objects.filter(first_name = st['first_name']).delete()

        data = serializers.serialize('json', Student.objects.all())
        return JsonResponse(json.loads(data), safe= False)



class StudentViewParams(View):
    def get (self, request):
        data = serializers.serialize('json', Student.objects.all())
        return JsonResponse(json.loads(data), safe= False)

    
    def put(self, request, *args, **kwargs):
        st = json.loads(request.body)
        to = request.GET.get('pk')
        print(to)
        Student.objects.filter(pk = to).update(
            first_name = st['first_name'], 
            last_name = st['last_name'],
            age = st['age'],
            email = st['email']
        )
        data = serializers.serialize('json', Student.objects.all())
        return JsonResponse(json.loads(data), safe= False)

    
    def delete(self, request, *args, **kwargs):
        st = json.loads(request.body)
        to = request.GET.get('pk')
        Student.objects.filter(pk = to).delete()

        data = serializers.serialize('json', Student.objects.all())
        return JsonResponse(json.loads(data), safe= False)
