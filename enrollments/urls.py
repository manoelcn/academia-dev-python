from django.urls import path
from .views import EnrollmentListView


urlpatterns = [
    path('enrollments/list/', EnrollmentListView.as_view(), name='enrollment-list'),
]