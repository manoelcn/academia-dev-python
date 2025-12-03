from django.shortcuts import render
from courses.models import Course
from enrollments.models import Enrollment
from students.models import Student


def home_page(request):
    total_student = Student.objects.count()
    active_courses = Course.objects.filter(status=True).count()
    paid_enrollments = Enrollment.objects.filter(status='pago').count()
    pending_enrollments = Enrollment.objects.filter(status='pendente').count()
    context = {
        'total_student': total_student,
        'active_courses': active_courses,
        'paid_enrollments': paid_enrollments,
        'pending_enrollments': pending_enrollments
    }
    return render(request, 'home.html', context)