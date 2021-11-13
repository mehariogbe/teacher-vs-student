from django.contrib import admin
from .models import User, Student, Teacher, Course, Lesson, Lab
# Register your models here.

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Lab)