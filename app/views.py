from django.db.models import fields
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Comment, Deliverable, Lab, User, Student, Teacher, Course, Lesson
from .form import StudentSignUpForm, TeacherSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



# Create your views here.


class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["courses"] = Course.objects.all()
        return context

@method_decorator(login_required,  name='dispatch')
class TeacherProfile(TemplateView):
    template_name = "teachers_profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["courses"] = Course.objects.all()
        return context

@method_decorator(login_required,  name='dispatch')
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

# Views for Courses

@method_decorator(login_required,  name='dispatch')
class Course_list(TemplateView):
    template_name = "course_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["courses"] = Course.objects.all()
        return context

@method_decorator(login_required,  name='dispatch')
class CourseDetail(DetailView):
    model = Course
    template_name = "course_detail.html"
    

# Views for Lesson

@method_decorator(login_required,  name='dispatch')
class LessonCreate(View):

    def post(self, request, pk):
        title = request.POST.get("title")
        description = request.POST.get("description")
        course = Course.objects.get(pk=pk)
        Lesson.objects.create(
            title=title, description=description, course=course)
        return redirect('course_detail', pk=pk)


class LessonEdit(UpdateView):
    model = Lesson
    fields = ["title", "description", "course"]
    template_name = "lesson_edit.html"

    def get_success_url(self):
        return reverse('lesson_detail', kwargs={'pk': self.object.pk})


class LessonDelete(DeleteView):
    model = Lesson
    template_name = "lesson_delete.html"
    success_url = "/class/"

@method_decorator(login_required,  name='dispatch')
class Lesson_detail(DetailView):
    model = Lesson
    template_name = "lesson_detail.html"

# Views for ClassRoom

@method_decorator(login_required,  name='dispatch')
class ClassRoom(TemplateView):
    template_name = "class.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lessons"] = Lesson.objects.all()
        context["labs"] = Lab.objects.all()
        return context


# Views for Lab

class LabCreate(CreateView):

    def post(self, request, pk):
        types = request.POST.get("types")
        title = request.POST.get("title")
        description = request.POST.get("description")
        course = Course.objects.get(pk=pk)
        lab_deliverable = request.POST.get('lab_deliverable')
        if lab_deliverable == 'on':
            lab_deliverable = True
        else:
            lab_deliverable = False
        Lab.objects.create(types=types, title=title, description=description,
                           course=course, lab_deliverable=lab_deliverable)
        return redirect('course_detail', pk=pk)


@method_decorator(login_required,  name='dispatch')
class Lab_detail(DetailView):
    model = Lab
    template_name = "lab_detail.html"


class LabEdit(UpdateView):
    model = Lab
    fields = ["types", "title", "description", "course", "lab_deliverable"]
    template_name = "lab_edit.html"

    def get_success_url(self):
        return reverse('lab_detail', kwargs={'pk': self.object.pk})


class LabDelete(DeleteView):
    model = Lab
    template_name = "lab_delete.html"
    success_url = "/class/"

# Views for deliverables


class DeliverableCreate(CreateView):
    
    def post(self, request, pk):
        user = self.request.user
        title = request.POST.get("title")
        description = request.POST.get("description")
        lab = Lab.objects.get(pk=pk)
        Deliverable.objects.create(
            title=title, description=description, lab=lab, user=user)
        return redirect('lab_detail', pk=pk)
@method_decorator(login_required,  name='dispatch')
class DeliverablePage(TemplateView):
    template_name = "deliverables.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["deliverables"] = Deliverable.objects.all()
        
        return context
@method_decorator(login_required,  name='dispatch')
class Deliverable_detail(DetailView):
    model = Deliverable
    template_name = "deliverable_detail.html"        
    
#  Views For Comment
@method_decorator(login_required,  name='dispatch')
class CommentCreate(CreateView):
    model = Comment
    template_name = "comment_create.html"
    fields = ('comment',)

    def post(self, request, pk):
        author = self.request.user
        comment = request.POST.get("comment")
        lesson = Lesson.objects.get(pk=pk)
        Comment.objects.create(author=author, comment=comment, lesson=lesson)
        return redirect('lesson_detail', pk=pk)

class CommentEdit(UpdateView):
    model = Comment
    template_name = "comment_edit.html"
    fields = ('comment',)

    def get_success_url(self):
        lesson = self.object.lesson
        return reverse_lazy('lesson_detail', kwargs={'pk': lesson.id }) 

class CommentDelete(DeleteView):
    model = Comment
    template_name = "comment_delete.html"

    def get_success_url(self):
        lesson = self.object.lesson
        return reverse_lazy('lesson_detail', kwargs={'pk': lesson.id })
  

