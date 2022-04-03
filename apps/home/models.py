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
    email = models.EmailField()
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
    photo = models.ImageField(upload_to='media/photos/')
    data = models.DateField(default='')
    # estimation = models.

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Teachers(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField()
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
    photo = models.ImageField(upload_to='media/photos/')
    place_of_birth = models.CharField(max_length=128, default="не указан(а)")
    adress = models.CharField(max_length=128, default="не указан(а)")
    data = models.DateField(default='')
    # estimation = models.
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


