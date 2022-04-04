# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import Teachers,Students,Profession,Fakultet, Subjects, GroupNum,Time,Days,Schedule
admin.site.register(Teachers)
admin.site.register(Students)
admin.site.register(Profession)
admin.site.register(Fakultet)
admin.site.register(Subjects)
admin.site.register(Time)

admin.site.register(Days)
admin.site.register(GroupNum)
admin.site.register(Schedule)
