from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('register/',views.Register.as_view(), name='register'),
    path('teacher_signup/',views.teacher_signup.as_view(), name='teacher_signup'),
    path('student_signup/',views.student_signup.as_view(), name='student_signup'),



]