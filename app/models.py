from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.username

class Teacher(models.Model):
    
     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
     img = models.CharField(max_length=250)
     created_at = models.DateTimeField(auto_now_add=True) 

class Student(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    img = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)            