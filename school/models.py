from django.db import models

# Create your models here.

class Parent(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Subject(models.Model):
    name = models.CharField(max_length = 50)
    code = models.CharField(max_length = 100)

    def __str__(self):
        return f'{self.name}'


class Student(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    age = models.IntegerField()
    mark = models.IntegerField()
    parent = models.ForeignKey(Parent,on_delete = models.CASCADE)
    subjects = models.ManyToManyField(Subject)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        constraints = [
            models.CheckConstraint(
                name = 'age must be greater than 5', check = models.Q(age__gt = 5)
            ),
            models.CheckConstraint(
                name = 'mark must be greater than 0', check = models.Q(mark__gt = 0)
            ) 
        ]



