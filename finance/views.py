from django.shortcuts import render
from courses.models import Course
from enrollments.models import Enrollment
from students.models import Student
from django.views.generic import ListView


def finance(request):
    return render(request, 'finance.html', {})

def enrollments_by_status(request):
    status = request.GET.get('status')
    options = ['pago', 'pendente']
    if status in options:
        enrollments = Enrollment.objects.filter(status=status)
    else:
        enrollments = Enrollment.objects.all()
    context = {'enrollments': enrollments}
    return render(request, 'enrollments_by_status.html', context)
