from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Student
        fields = '__all__'

class MarksSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Marks
        fields = '__all__'
