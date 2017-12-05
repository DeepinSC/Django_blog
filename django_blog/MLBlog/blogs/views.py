# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.sessions.models import Session
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from rest_framework import permissions, mixins, authentication
from rest_framework.response import Response
from rest_framework import viewsets
from models import Blogs
from rest_framework import generics
from serializers import BlogsSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
import permissions
# Create your views here.


class BlogsViewSet(viewsets.ModelViewSet):
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerializer
    #permission_classes = (permissions.IsOwnerOrReadOnly,)
    #authentication_classes = (SessionAuthentication, BasicAuthentication)



    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)



@csrf_exempt
def login(request):
    return render(request,'blogs/login.html')

@csrf_exempt
def blogs(request):
    user = request.user
    return render(request,'blogs/blogs.html',{"user":user,})

@csrf_exempt
def detail(request,pk):
    user = request.user
    return render(request,'blogs/detail.html',{"user":user,})
