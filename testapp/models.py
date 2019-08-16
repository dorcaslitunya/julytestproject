from django.db import models


# Create your models here.

class testdata(models.Model):
    studentName = models.CharField(max_length=30)
    course = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField()


def __str__(self):
    return self.studentName
