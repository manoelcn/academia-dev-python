from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(unique=True)
    cpf = models.CharField(unique=True, max_length=11)
    admission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
