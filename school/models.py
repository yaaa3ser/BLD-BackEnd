from django.db import models

# Create your models here.

class Parent(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Student(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    age = models.IntegerField()
    mark = models.IntegerField()
    parent = models.ForeignKey(Parent,on_delete = models.CASCADE, related_name = 'students')


    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    


