from rest_framework import serializers
from students.models import Student
from enrollments.models import Enrollment
from courses.serializers import CourseSerializer


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class StudentReportSerializer(serializers.Serializer):
    student_name = serializers.CharField()
    total_pending = serializers.DecimalField(max_digits=10, decimal_places=2)

class StudentEnrollmentsSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Enrollment
        fields = '__all__'
