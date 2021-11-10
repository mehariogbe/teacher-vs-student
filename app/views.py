from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from .models import User
from .form import StudentSignUpForm, TeacherSignUpForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"
    
# registration or signup

class Register(TemplateView):
    template_name = "registration/register.html"

class teacher_signup(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name= 'registration/teacher_signup.html'



class student_signup(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name= 'registration/student_signup.html'     