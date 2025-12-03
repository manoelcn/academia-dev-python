from django.views.generic import ListView, DetailView
from rest_framework import generics
from students.models import Student
from students.serializers import StudentSerializer
from enrollments.models import Enrollment


class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_detail.html'
    context_object_name = 'student'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student = self.object
        enrolled_courses = Enrollment.objects.filter(student=student)
        context['enrolled_courses'] = enrolled_courses

        paid_enrollments = Enrollment.objects.filter(status='pago', student_id=student)
        pending_enrollments = Enrollment.objects.filter(status='pendente', student_id=student)
        total_paid = sum(enrollment.course.enrollment_fee for enrollment in paid_enrollments)
        total_pending = sum(enrollment.course.enrollment_fee for enrollment in pending_enrollments)
        total = total_paid + total_pending
        context['total'] = total
        return context

class StudentCreateListAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
