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

def get_financial_status(request, pk):
    student = Student.objects.get(pk=pk)
    paid_enrollments = Enrollment.objects.filter(status='pago', student_id=student)
    pending_enrollments = Enrollment.objects.filter(status='pendente', student_id=student)
    total_paid = sum(enrollment.course.enrollment_fee for enrollment in paid_enrollments)
    total_pending = sum(enrollment.course.enrollment_fee for enrollment in pending_enrollments)

    context = {
        'student': student,
        'total_paid': total_paid,
        'total_pending': total_pending
        }
    return render(request, 'student_finance.html', context)