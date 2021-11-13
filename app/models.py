from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Teacher(models.Model):
    
     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
     img = models.CharField(max_length=250)
     created_at = models.DateTimeField(auto_now_add=True) 

class Student(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    img = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)            


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image  = models.CharField(max_length=1000)
    description = models.CharField(max_length=9999)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # students = models.ManyToManyField(Student)
    # teachers = models.ManyToManyField(Teacher)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=9999)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Lab(models.Model):
    LAB_TYPES =(
        ('Lab', 'Lab'),
        ('Homework', 'Homework'),
        ('Project', 'Project'),
    )
    id = models.AutoField(primary_key=True)
    types = models.CharField(max_length=20, choices=LAB_TYPES)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=9999)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="labs")
    lab_deliverable = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
