from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from students.models import Student
from .serializers import (
    StudentSerializer,
    StudentWriteSerializer,
    CustomTokenObtainPairSerializer,
)


class ApiHomeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "message": "Welcome to the Student Management API"
        })


class StudentListCreateAPI(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.select_related(
        "user",
        "department"
    ).prefetch_related("courses")

    def get_serializer_class(self):
        if self.request.method == "POST":
            return StudentWriteSerializer
        return StudentSerializer


class StudentRetrieveUpdateDestroyAPI(
    generics.RetrieveUpdateDestroyAPIView
):
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.select_related(
        "user",
        "department"
    ).prefetch_related("courses")

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return StudentWriteSerializer
        return StudentSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = []  # No authentication needed to get token
    serializer_class = CustomTokenObtainPairSerializer

    def get(self, request, *args, **kwargs):
        username = request.query_params.get("username")
        password = request.query_params.get("password")
        if username and password:
            serializer = self.get_serializer(data={"username": username, "password": password})
            try:
                serializer.is_valid(raise_exception=True)
                return Response(serializer.validated_data)
            except Exception as e:
                return Response({"error": str(e)}, status=400)
        return Response({
            "message": "To obtain a token, send a POST request with 'username' and 'password', or query via GET with ?username=xxx&password=yyy"
        })