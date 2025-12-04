from rest_framework import serializers
from students.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class StudentReportSerializer(serializers.Serializer):
    student_name = serializers.CharField()
    total_pending = serializers.DecimalField(max_digits=10, decimal_places=2)
