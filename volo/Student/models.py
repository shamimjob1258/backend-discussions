from django.db import models

class Student(models.Model) :
    name = models.CharField(max_length=20, null=False, blank=False)
    age = models.IntegerField(default=0, null=True, blank=True)
    standard = models.CharField(max_length=3, null=True, blank=True)
    # studentmarks = models.ManyToManyField(Marks, related_name="stu_marks")

class Marks(models.Model) :
    subject = models.CharField(max_length=20, null=False, blank=False)
    marks = models.IntegerField(default=0, null=True, blank=True)
    student = models.ManyToManyField(Student, related_name="studentmarks")
