from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from students.models import Student,Department,course

class DashbaordAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        return Response({
            'student_count':Student.objects.count(),
            'Department_count':Department.objects.count(),
            'course_count': course.objects.count(),
        })