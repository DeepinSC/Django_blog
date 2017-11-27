# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=100, default='')
    created_time = models.DateTimeField(auto_now_add=True)
    #author = models.ForeignKey('auth.User', related_name='blogs', on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    category = models.CharField(max_length=20)
    tag = models.CharField(max_length=20)
    modify_time = models.DateTimeField(auto_now_add=True,blank=True)


