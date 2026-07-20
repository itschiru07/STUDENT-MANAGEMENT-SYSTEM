from rest_framework import serializers
from students.models import Student, Department,course
from accounts.models import CustomUser
from rest_framework import generics
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "phone",
            "role",
        ]


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = "__all__"
        
class courseSerializer(serializers.ModelSerializer):

    class Meta:
        model = course
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    department = DepartmentSerializer(read_only=True)
    courses = courseSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = [
            "id",
            "user",
            "first_name",
            "last_name",
            "email",
            "phone",
            "dob",
            "gender",
            "cgpa",
            "photo",
            "department",
            "courses",
        ]

class StudentWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            "id",
            "user",
            "first_name",
            "last_name",
            "email",
            "phone",
            "dob",
            "gender",
            "cgpa",
            "photo",
            "department",
            "courses",
        ]


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        data["user"] = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "firstname": user.first_name,
            "lastname": user.last_name,
            "phone": user.phone,
            "role": user.role,
        }
        return data