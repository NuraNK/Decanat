# -*- encoding: utf-8 -*-f
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

class Subjects(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.name

class Fakultet(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Profession(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Students(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    fakultet = models.ForeignKey(
        Fakultet,
        on_delete=models.CASCADE
    )
    profession = models.ForeignKey(
        Profession,
        on_delete=models.CASCADE
    )
    subjects = models.ManyToManyField(
        Subjects,
        default=''
    )
    place_of_birth = models.CharField(max_length=128, default="не указан(а)")
    adress = models.CharField(max_length=128, default="не указан(а)")
    photo = models.ImageField(upload_to='photos/', default='/media/photos/marc.jpg')

    data = models.DateField(default='')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Teachers(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    fakultet = models.ForeignKey(
        Fakultet,
        on_delete=models.CASCADE
    )
    profession = models.ForeignKey(
        Profession,
        on_delete=models.CASCADE
    )
    subjects = models.ManyToManyField(
        Subjects,
        default=''
    )
    students = models.ManyToManyField(
        Students
    )
    photo = models.ImageField(upload_to='media/photos/', default='/media/photos/marc.jpg')
    place_of_birth = models.CharField(max_length=128, default="не указан(а)")
    adress = models.CharField(max_length=128, default="не указан(а)")
    data = models.DateField(default='')
    # estimation = models.
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class GroupNum(models.Model):
    group = models.CharField(max_length=5)
    students = models.ManyToManyField(Students)
    teachers = models.ManyToManyField(Teachers)

    def __str__(self):
        return self.group


class Time(models.Model):
    time = models.CharField(max_length=128)

    def __str__(self):
        return self.time

class Days(models.Model):
    DAY = (
        ("ПН","ПН"),
        ("ВТ", "ВТ"),
        ("СР", "СР"),
        ("ЧТ", "ЧТ"),
        ("ПТ", "ПТ"),
        ("СБ", "СБ"),
    )
    day = models.CharField(max_length=128, choices=DAY)

    def __str__(self):
        return self.day


class Schedule(models.Model):
    group_num = models.ForeignKey(
        GroupNum,
        on_delete=models.CASCADE
    )
    time = models.ForeignKey(
        Time,
        on_delete=models.CASCADE
    )
    day = models.ForeignKey(
        Days,
        on_delete=models.CASCADE
    )
    subjects = models.ForeignKey(
        Subjects,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.group_num} - {self.time} - {self.day} - {self.subjects}'