from django.views.generic import ListView
from .models import Enrollment


class EnrollmentListView(ListView):
    model = Enrollment
    template_name = 'enrollment_list.html'
    context_object_name = 'enrollments'
