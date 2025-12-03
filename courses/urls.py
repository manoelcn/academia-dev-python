from django.urls import path
from .views import CourseListView, CourseCreateListAPIView, CourseRetriveUpdateDestroyAPIView


urlpatterns = [
    path('courses/list/', CourseListView.as_view(), name='course-list'),

    path('api/v1/courses/', CourseCreateListAPIView.as_view(), name='course-create-list-api'),
    path('api/v1/courses/<int:pk>/', CourseRetriveUpdateDestroyAPIView.as_view(), name='course-detail-api'),
]