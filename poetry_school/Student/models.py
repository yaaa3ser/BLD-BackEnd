from statistics import mode
from sys import maxsize
from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    age = models.IntegerField()
    email = models.EmailField()


    def __str__(self):
        return self.first_name + self.last_name

    