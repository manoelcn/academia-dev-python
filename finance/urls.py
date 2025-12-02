from django.urls import path
from .views import enrollments_by_status, get_financial_status

urlpatterns = [
    path('finance/enrollments/', enrollments_by_status, name='finance-enrollments'),
    path('finance/<int:pk>/', get_financial_status , name='finance-student'),
]