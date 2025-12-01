from django.urls import path
from .views import CourseListView


urlpatterns = [
    path('courses/list/', CourseListView.as_view(), name='course-list'),
]