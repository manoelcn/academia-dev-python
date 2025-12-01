from django.db import models
from courses.models import Course
from students.models import Student


class Enrollment(models.Model):
    STATUS_CHOICE = [
        ('pago', 'Pago'),
        ('pendente', 'Pendente'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='matriculas')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='matriculas')
    enrollment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='pendente')

    def __str__(self):
        return f"{self.student.name} - {self.course.name}"
