from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    address=models.CharField(max_length=122)
    field=models.CharField(max_length=122)
    salary=models.CharField(max_length=12)
    date=models.DateField()

    def __str__(self):
        return self.name
