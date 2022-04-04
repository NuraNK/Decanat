# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    #Teachers
    path('teachers/list/',views.TeacherListView.as_view(), name='teachers-list'),
    path('teachers/<int:pk>/', views.TeacherDetailView.as_view(), name='teachers'),
    path('teachers/update/<int:pk>/', views.TeachersUpdateView.as_view(), name='teachers-update'),
    path('teachers/create/', views.create_teacher, name='teachers-create'),
    #Students
    path('students/create/', views.create_student, name='students-create'),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name='students'),
    path('students/list/', views.StudentListView.as_view(), name='students-list'),
    path('students/update/<int:pk>/', views.StudentUpdateView.as_view(), name='students-update'),

    path('map/', views.map, name='map-url'),
    path('notifications/', views.notifications, name='notifications-url'),
    path('schedule/', views.ScheduleListView.as_view(), name='schedule'),
    path('schedule-create/', views.create_schedule, name='schedule-create'),
    path('group-create/', views.GroupView.as_view(), name='group-create'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
