from django.urls import path
from enrollments.views import EnrollmentListView, EnrollmentCreateListAPIView


urlpatterns = [
    path('enrollments/list/', EnrollmentListView.as_view(), name='enrollment-list'),

    path('api/v1/enrollments/', EnrollmentCreateListAPIView.as_view(), name='enrollment-create-list-api'),
]