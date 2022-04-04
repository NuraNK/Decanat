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
from .form import TeacherForm, StudentForm, ScheduleForm, GroupNumForm
from .models import Students,Teachers, Profession,Subjects, Fakultet, Time, GroupNum, Schedule, Days
from .filters import TeachersFilter, ScheduleFilter, StudentFilter


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

class TeachersUpdateView(UpdateView):
    model = Teachers
    form_class = TeacherForm
    template_name = 'home/page-update-teacher.html'
    success_url = '/teachers/list/'

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
        context['filter'] = StudentFilter(self.request.GET, queryset=self.get_queryset())
        return context

class StudentDetailView(DetailView):
    template_name = 'home/students-detail.html'
    model = Students
    context_object_name = 'student'

class StudentUpdateView(UpdateView):
    model = Students
    form_class = StudentForm
    template_name = 'home/page-update-student.html'
    success_url = '/students/list/'



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


def map(request):
    return render(request, 'home/ui-maps.html')

def notifications(request):
    return render(request, 'home/ui-notifications.html')

class ScheduleListView(ListView):
    model = Schedule
    template_name = 'home/schedule.html'
    context_object_name = 'schedule'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(context)
        context['filter'] = ScheduleFilter(self.request.GET, queryset=self.get_queryset())
        # print(self.request.GET)
        time = Time.objects.all()
        day = Days.objects.all()
        day1 = Schedule.objects.filter(
            group_num=1,
            time_id=1
        )
        day2 = Schedule.objects.filter(
            group_num=1,
            time_id=2
        )
        day3 = Schedule.objects.filter(
            group_num=1,
            time_id=3
        )
        day4 = Schedule.objects.filter(
            group_num=1,
            time_id=4
        )
        context['time']=time
        context['day']=day
        context['day1'] = day1
        context['day2'] = day2
        context['day3'] = day3
        context['day4'] = day4
        return context

    #
    # def get_queryset(self):
    #     query = Schedule.objects.filter(group_num=1)
    #     return query


@csrf_exempt
@login_required(login_url="/login/")
def create_schedule(request):
    if request.method == 'POST':
        form_schedule = ScheduleForm(request.POST, request.FILES)
        if form_schedule.is_valid():
            # form.save()
            Schedule.objects.create(**form_schedule.cleaned_data)
            return redirect('schedule-create')
    else:
        form_schedule = ScheduleForm()
    return render(request, "home/schedule-create.html", {'form_schedule':form_schedule})

class GroupView(CreateView):
    model = GroupNum
    form_class = GroupNumForm
    template_name = 'home/group-create.html'
    success_url = '/group-create/'

