from django.db import models
from django.contrib.auth.models import AbstractUser
from .choices import *

# Create your models here.
class User(AbstractUser):
    user_type = models.CharField(choices=User_Types, max_length=60, default="")

    def __str__(self):
        return f"{self.username}"
    
class CustomGO(models.Model):
    type = models.CharField(choices=GO_Types, max_length=64, default="")
    name = models.CharField(max_length=64, default="")
    instruction = models.CharField(max_length=320, default="")
    numRows = models.IntegerField(blank=True, null=True)
    col1Title = models.CharField(max_length=64, default="")
    col2Title = models.CharField(max_length=64, default="")

    def __str__(self):
        return f"{self.name}"
    
class Assignments(models.Model):
    student_id = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    go_id = models.ForeignKey(CustomGO, on_delete=models.CASCADE, default="")
    assigned = models.DateTimeField(blank=True, null=True, verbose_name='assigned')
    completed = models.DateTimeField(blank=True, null=True, verbose_name='completed')
    graded = models.DateTimeField(blank=True, null=True, verbose_name='graded')
    grade = models.CharField(max_length=1, default="", null=True, blank=True)

    def __str__(self):
        return f"{self.id}: {self.student_id}"

class Data(models.Model):
    student_id = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    assignment_id = models.ForeignKey(Assignments, on_delete=models.CASCADE, default="", null=True, blank=True)
    go_id = models.ForeignKey(CustomGO, on_delete=models.CASCADE, default="")
    answer1 = models.CharField(max_length=650, default="", null=True, blank=True)
    answer2 = models.CharField(max_length=650, default="", null=True, blank=True)
    answer3 = models.CharField(max_length=650, default="", null=True, blank=True)
    answer4 = models.CharField(max_length=650, default="", null=True, blank=True)
    answer5 = models.CharField(max_length=650, default="", null=True, blank=True)
    answer6 = models.CharField(max_length=650, default="", null=True, blank=True)
    answer7 = models.CharField(max_length=650, default="", null=True, blank=True)
    answer8 = models.CharField(max_length=650, default="", null=True, blank=True)
    answer9 = models.CharField(max_length=650, default="", null=True, blank=True)
    answer10 = models.CharField(max_length=650, default="", null=True, blank=True)