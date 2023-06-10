from django.db import models

class Student2(models.Model):
    name=models.CharField(max_length=123)
    email=models.EmailField()
    contact=models.IntegerField(max_length=10)
    def __str__(self):
        return self.name
class Teacher(models.Model):
    name=models.CharField(max_length=123)
    email=models.EmailField()
    contact=models.IntegerField(max_length=10)
    def __str__(self):
        return self.name