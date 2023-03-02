from django.db import models

# Create your models here.
class Employees(models.Model):
    name=models.CharField(max_length=200)
    rollno=models.TextField(max_length=500)
    Intime=models.TextField()
    Outtime=models.TextField()
    nodeno=models.IntegerField()

    def __str__(self) -> str:
        return self.name