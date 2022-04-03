# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('filter/', views.Filter.as_view(), name='filter_teacher'),
    #Teachers
    path('teachers/list/',views.TeacherListView.as_view(), name='teachers-list'),
    path('teachers/<int:pk>/', views.TeacherDetailView.as_view(), name='teachers'),
    path('teachers/update/<id>/', views.update_view, name='teachers-update'),
    path('teachers/create/', views.create_teacher, name='teachers-create'),
    #Students
    path('students/create/', views.create_student, name='students-create'),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name='students'),
    path('students/list/', views.StudentListView.as_view(), name='students-list'),
    path('students/update/<id>/', views.student_update_view, name='students-update'),
    path('students/delete/<int:pk>/', views.student_update_view, name='students-delete'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
