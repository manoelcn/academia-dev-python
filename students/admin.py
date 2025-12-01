from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'cpf', 'admission_date')
    search_fields = ('name', 'email', 'cpf')
    list_filter = ('admission_date',)
