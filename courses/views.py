from django.views.generic import ListView
from rest_framework import generics
from courses.models import Course
from courses.serializers import CourseSerializer


class CourseListView(ListView):
    model = Course
    template_name = 'course_list.html'
    context_object_name = 'courses'

class CourseCreateListAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseRetriveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
