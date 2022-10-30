from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import Student, Parent


def check_age(age):
    if age <= 5:
        raise ValidationError("age must be older than 5")
    
def check_mark(mark):
    if mark <= 0:
        raise ValidationError("mark must be positive")

class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class ParentSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    students = StudentListSerializer(many = True)
    class Meta:
        model = Parent
        fields = '__all__'
     
# this class is to return only name of parent of each student   
# ==> to prevent returning students of each parent when searching for students. 
class Parent__Serializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    class Meta:
        model = Parent
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    age = serializers.IntegerField(validators=[check_age])
    mark = serializers.IntegerField(validators=[check_mark])
    parent = Parent__Serializer()
    
    class Meta:
        model = Student
        fields = '__all__'
