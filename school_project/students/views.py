from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Bienvenue 🎓</h1><p>API disponible sur /api/students/</p>")
from django.shortcuts import render

def home(request):
    return render(request, "students/home.html")
