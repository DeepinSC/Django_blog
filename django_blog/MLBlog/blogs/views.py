# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from rest_framework import permissions, mixins
from rest_framework.response import Response
from rest_framework import viewsets
from models import Blogs
from rest_framework import generics
from serializers import BlogsSerializer
# Create your views here.

class BlogsViewSet(viewsets.ModelViewSet):
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerializer
    #permission_classes = (permissions.IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

@csrf_exempt
def index(request):
    return render_to_response('blogs/index.html',{},RequestContext(request))

@csrf_exempt
def login(request):
    return render(request,'blogs/login.html')
