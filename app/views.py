from django.db.models import fields
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .models import User, Student, Teacher, Course, Lesson
from .form import StudentSignUpForm, TeacherSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# Create your views here.


class Home(TemplateView):
    template_name = "home.html"


class TeacherProfile(TemplateView):
    template_name = "teachers_profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["courses"] = Course.objects.all()
        return context


class StudentsProfile(TemplateView):
    template_name = "students_profile.html"


# registration or signup

class Register(TemplateView):
    template_name = "registration/register.html"


class teacher_signup(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'registration/teacher_signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/teachers')


class student_signup(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'registration/student_signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/students')


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_student:
                    login(request, user)
                    return redirect('/students')
                else:
                    login(request, user)
                    return redirect('/teachers')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')

    return render(request, 'registration/login.html',
                  context={'form': AuthenticationForm()})


def logout_view(request):
    logout(request)
    return redirect('/')

# Courses


class Course_list(TemplateView):
    template_name = "course_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["courses"] = Course.objects.all()
        return context


class CourseDetail(DetailView):
    model = Course
    template_name = "course_detail.html"

class LessonCreate(View):

    def post(self, request, pk):
        title = request.POST.get("title")
        description = request.POST.get("description")
        course = Course.objects.get(pk=pk)
        Lesson.objects.create(title=title, description=description, course=course)
        return redirect('course_detail', pk=pk)
class LessonEdit(UpdateView):
    model = Lesson
    fields = ["title", "description", "course"]
    template_name = "lesson_edit.html"
    success_url = "/class/"
    
    # def get_success_url(self ):
        
    #     return reverse('course_detail', kwargs={'pk': self.object.pk})

class LessonDelete(DeleteView):
    model = Lesson
    template_name = "lesson_delete.html"
    success_url = "/class/"


class ClassRoom(TemplateView):
    template_name = "class.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lessons"] = Lesson.objects.all()
        return context
