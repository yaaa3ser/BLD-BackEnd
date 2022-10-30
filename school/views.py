from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Student, Parent
from .serializers import StudentSerializer, ParentSerializer

# Create your views here.


class StudentView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # def get(self, request):
    #     data = StudentSerializer(Student.objects.all(), many=True)
    #     return Response(data.data)

    # def post(self, request):
    #     serializer = StudentSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)
    
class StudentDetailView(generics.RetrieveAPIView,generics.DestroyAPIView,generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # def get(self, request, id):
    #     try:
    #         data = StudentSerializer(Student.objects.get(id=id))
    #         return Response(data.data)
    #     except:
    #         return Response(status = status.HTTP_404_NOT_FOUND)

    # def put(self, request, id):
    #     try:
    #         serializer = StudentSerializer(data=request.data,
    #                                     instance=Student.objects.get(id=id))
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data)
    #         return Response(serializer.errors)
    #     except:
    #         return Response(status = status.HTTP_404_NOT_FOUND)

    # def delete(self, request, id):
    #     try:
    #         Student.objects.get(id=id).delete()
    #         return Response(status = status.HTTP_200_OK)
    #     except:
    #         return Response(status = status.HTTP_404_NOT_FOUND)
    
class ParentView(generics.ListCreateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

class ParentDetailView(generics.RetrieveAPIView,generics.DestroyAPIView,generics.UpdateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer