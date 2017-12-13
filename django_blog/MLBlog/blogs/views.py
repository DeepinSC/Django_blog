# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from rest_framework import permissions, mixins, authentication
from rest_framework.response import Response
from rest_framework import viewsets

from .permissions import IsOwnerOrReadOnly
from .models import Blogs
from rest_framework import generics
from .serializers import BlogsSerializer
from django.utils import timezone
import markdown
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# Create your views here.


class BlogsViewSet(viewsets.ModelViewSet):
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

    def perform_update(self, serializer):
        serializer.save(modify_time = timezone.now()) #更改时更新到当前时间


@csrf_exempt
def blogs(request):
    return render(request,'blogs/blogs.html')

@csrf_exempt
def detail(request,pk):
    return render(request,'blogs/detail.html')

def edit(request,pk):
    return render(request, 'blogs/edit.html')

def newblog(request):
    return render(request, 'blogs/edit.html')
