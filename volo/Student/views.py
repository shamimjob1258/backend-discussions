from django.shortcuts import render
from .models import Student, Marks
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

class Students(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

class StudentMarks(viewsets.ModelViewSet) :
    queryset = Marks.objects.all()
    serializer_class=MarksSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'subject']
