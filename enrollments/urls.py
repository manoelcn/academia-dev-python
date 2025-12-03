from django.urls import path
from enrollments.views import EnrollmentListView, EnrollmentCreateListAPIView, EnrollmentRetriveUpdateAPIView


urlpatterns = [
    path('enrollments/list/', EnrollmentListView.as_view(), name='enrollment-list'),

    path('api/v1/enrollments/', EnrollmentCreateListAPIView.as_view(), name='enrollment-create-list-api'),
    path('api/v1/enrollments/<int:pk>/', EnrollmentRetriveUpdateAPIView.as_view(), name='enrollment-detail-api'),
]