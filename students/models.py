from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    grade = models.CharField(max_length=20)
    enrolled_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
