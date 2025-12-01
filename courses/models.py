from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=200)
    duration_hours = models.IntegerField()
    enrollment_fee = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
