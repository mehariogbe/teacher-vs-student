from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


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
    path('courses/<int:pk>/', views.CourseDetail.as_view(), name="course_detail"),

    path('courses/<int:pk>/lessons/add/', views.LessonCreate.as_view(), name="lesson_create"),
    path('lesson/<int:pk>/', views.Lesson_detail.as_view(), name="lesson_detail"),
    path('lesson/<int:pk>/edit/', views.LessonEdit.as_view(), name="lesson_edit"),
    path('lesson/<int:pk>/delete', views.LessonDelete.as_view(), name="lesson_delete"),
    
    path('class/', views.ClassRoom.as_view(), name='class'),

    path('courses/<int:pk>/labs/add', views.LabCreate.as_view(), name="lab_create"),
    path('lab/<int:pk>/', views.Lab_detail.as_view(), name="lab_detail"),
    path('lab/<int:pk>/edit/', views.LabEdit.as_view(), name="lab_edit"),
    path('lab/<int:pk>/delete', views.LabDelete.as_view(), name="lab_delete"),

    path('lab/<int:pk>/deliverable',views.DeliverableCreate.as_view(), name="deliverable_create"),
    path('deliverable/', views.DeliverablePage.as_view(), name='deliverable'),

    path('lesson/<int:pk>/comment',views.CommentCreate.as_view(), name="comment_create"),
    path('lesson/<int:pk>/comment_edit',views.CommentEdit.as_view(), name="comment_edit"),
    path('lesson/<int:pk>/comment_delete',views.CommentDelete.as_view(), name="comment_delete"),



]