from django.urls import path
from . import views


urlpatterns = [
    path('students/list/', views.StudentListView.as_view(), name='student-list'),
    path('students/<int:pk>/detail/', views.StudentDetailView.as_view(), name='student-detail'),

    path('api/v1/students/', views.StudentCreateListAPIView.as_view(), name='student-create-list-api'),
    path('api/v1/students/<int:pk>/', views.StudentRetriveUpdateDestroyAPIView.as_view(), name='student-detail-api'),
]