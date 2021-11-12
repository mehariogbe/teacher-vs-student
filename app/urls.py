from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('register/',views.Register.as_view(), name='register'),
    path('teacher_signup/',views.teacher_signup.as_view(), name='teacher_signup'),
    path('student_signup/',views.student_signup.as_view(), name='student_signup'),
    path('login/',views.login_request, name='login'),
    path('logout/',views.logout_view, name='logout'),

    path('teachers/', views.TeacherProfile.as_view(), name="teachers_profile"),
    path('students/', views.StudentsProfile.as_view(), name="students_profile"),
    path('courses/', views.Course_list.as_view(), name='courses'),



]