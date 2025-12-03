from django.urls import path
from . import views


urlpatterns = [
    path('students/list/', views.StudentListView.as_view(), name='student-list'),
    path('students/<int:pk>/detail/', views.StudentDetailView.as_view(), name='student-detail'),
]