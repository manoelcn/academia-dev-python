from django.urls import path
from .views import enrollments_by_status

urlpatterns = [
    path('finance/enrollments/', enrollments_by_status, name='finance-enrollments'),
]