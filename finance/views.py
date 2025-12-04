from django.shortcuts import render, get_object_or_404
from courses.models import Course
from enrollments.models import Enrollment
from students.models import Student
from django.views.generic import ListView


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
    student = get_object_or_404(Student, pk=pk)
    sql = """
        SELECT 
            enrollment.id,
            enrollment.status,
            SUM(course.enrollment_fee) AS total
        FROM enrollments_enrollment AS enrollment
        JOIN courses_course AS course 
            ON course.id = enrollment.course_id
        WHERE enrollment.student_id = %s
        GROUP BY 
            enrollment.id,
            enrollment.status;
    """
    rows = Enrollment.objects.raw(sql, [pk])
    total_paid = 0
    total_pending = 0
    for row in rows:
        if row.status == 'pago':
            total_paid += row.total
        else:
            total_pending += row.total
    context = {
        'student': student,
        'total_paid': total_paid,
        'total_pending': total_pending
    }
    return render(request, 'student_finance.html', context)