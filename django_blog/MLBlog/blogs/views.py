# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import viewsets
from models import Blogs
from serializers import BlogsSerializer
# Create your views here.

class BlogsViewSet(viewsets.ModelViewSet):
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerializer
    #permission_classes = (permissions.IsAuthenticated,)


def index(request):
    return render(request,'blogs/index.html')