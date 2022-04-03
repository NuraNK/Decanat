# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.views.decorators.csrf import csrf_exempt
from django import template
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.urls import reverse
from django.views.generic import DetailView, UpdateView, CreateView, ListView, DeleteView
from .form import TeacherForm, StudentForm
from .models import Students,Teachers, Profession,Subjects, Fakultet
from .filters import TeachersFilter

@csrf_exempt
@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


class TeacherListView(ListView):
    model = Teachers
    template_name = 'home/ui-teachers-list.html'
    context_object_name = 'teacher'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(context)
        context['filter'] = TeachersFilter(self.request.GET, queryset=self.get_queryset())
        return context
# a = TeacherListView

class TeacherDetailView(DetailView):
    template_name = 'home/page-user.html'
    model = Teachers
    context_object_name = 'teacher'

@csrf_exempt
def update_view(request, id):
    context = {}
    obj = get_object_or_404(Teachers, id=id)
    form = TeacherForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)
    context["form"] = form
    return render(request, "home/page-update-teacher.html", context)

@csrf_exempt
@login_required(login_url="/login/")
def create_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            Teachers.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form = TeacherForm()
    return render(request, "home/page-teacher-create.html", {'form':form})

# @login_required(login_url="/login/")
class StudentListView(ListView):
    model = Students
    template_name = 'home/ui-student_list.html'
    context_object_name = 'student-list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(context)
        context['filter'] = TeachersFilter(self.request.GET, queryset=self.get_queryset())
        return context

class StudentDetailView(DetailView):
    template_name = 'home/students-detail.html'
    model = Students
    context_object_name = 'student'

@csrf_exempt
def student_update_view(request, id):
    context = {}
    obj = get_object_or_404(Students, id=id)
    form = StudentForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)
    context["form"] = form
    return render(request, "home/page-update-student.html", context)

@csrf_exempt
@login_required(login_url="/login/")
def delete_student(request, pk):
    query = Students.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        return redirect('students-list')
    return render(request, 'home/page-update-student.html',{'query':query})

@csrf_exempt
@login_required(login_url="/login/")
def create_student(request):
    if request.method == 'POST':
        forma = StudentForm(request.POST, request.FILES)
        if forma.is_valid():
            # print(form.cleaned_data)
            # form.save()
            Students.objects.create(**forma.cleaned_data)
            return redirect('students-create')
    else:
        forma = StudentForm()
    return render(request, "home/page-student-create.html", {'forma':forma})



@csrf_exempt
@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


class Filter(ListView):

    def get_queryset(self):
        queryset = Profession.objects.filter(
            name__in=self.request.GET.get('name')
        )
        return queryset