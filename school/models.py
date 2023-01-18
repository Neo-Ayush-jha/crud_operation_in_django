from django.db import models
CITY = (
    ("Purnea", "Purnea"),
    ("Patna", "Patna"),
    ("Bhagalpur", "Bhagalpur"),
    ("Bhopal", "Bhopal"),
    ("indore", "indore"),
    ("Delhi", "Delhi"),
    ("Kolkata", "Kolkata"),
    ("Pune", "Pune"),
    ("Goa", "Goa"),
    ("Jalandher", "Jalandher"),
    ("Dharbhanga", "Dharbhanga"),
    ("Rachi", "Rachi"),
)
class Student2(models.Model):
    name=models.CharField(max_length=123)
    email=models.EmailField()
    contact=models.IntegerField(max_length=10)
    city=models.CharField(max_length=123,choices=CITY)
    def __str__(self):
        return self.name