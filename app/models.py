from django.db import models

# Create your models here.

class Employee(models.Model):
    Eid=models.IntegerField(primary_key=True)
    Ename=models.CharField(max_length=100)
    Eage=models.IntegerField()

    def __str__(self) -> str:
        return self.Ename
