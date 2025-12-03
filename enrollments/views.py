from django.views.generic import ListView
from rest_framework import generics
from enrollments.models import Enrollment
from enrollments.serializers import EnrollmentSerializer


class EnrollmentListView(ListView):
    model = Enrollment
    template_name = 'enrollment_list.html'
    context_object_name = 'enrollments'

class EnrollmentCreateListAPIView(generics.ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
