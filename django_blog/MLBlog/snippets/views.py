# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, renderers
from rest_framework.reverse import reverse
from permissons import IsOwnerOrReadOnly
from models import Snippets
from serializers import SnippetSerializer,UserSerializer

# Create your views here.

# @api_view(['GET','POST'])
# def snippet_list(request,format = None):
#     if request.method=='GET':
#         snippets = Snippets.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)
#     elif request.method=='POST':
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#

# @api_view(['GET','PUT','DELETE'])
# def snippet_detail(request,pk,format = None):
#     try:
#         snippet = Snippets.objects.get(pk=pk)
#     except Snippets.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

"""
Now We use the class-based view.
"""
# from rest_framework.views import APIView
#
# class SnippetList(APIView):
#     def get(self,request,format = None):
#         snippets = Snippets.objects.all()
#         serializer = SnippetSerializer(snippets,many=True)
#         return Response(serializer.data)
#     def post(self,request,format = None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class Snippet_detail(APIView):
#     def get_objects(self,pk):
#         try:
#             snippet = Snippets.objects.get(pk=pk)
#         except Snippets.DoesNotExist:
#             raise Http404
#
#     def get(self,request,pk,format=None):
#         snippet = self.get_objects(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
#
#     def put(self,request,pk,format = None):
#         snippet = self.get_objects(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         snippet = self.get_objects(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

"""
Then We go to Mixin classes. They are similar to TEMPLATES part in Django.
"""
# from rest_framework import mixins
# from rest_framework import generics
#
# class SnippetList(mixins.CreateModelMixin,mixins.ListModelMixin,generics.GenericAPIView):
#     queryset = Snippets.objects.all()
#     serializer_class = SnippetSerializer
#
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
# class SnippetDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Snippets.objects.all()
#     serializer_class = SnippetSerializer
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# """
# What if there is a more concise way? Yes.
# """
# from rest_framework import generics
# from rest_framework import permissions
#
# class SnippetList(generics.ListCreateAPIView):
#     queryset = Snippets.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Snippets.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,
#                           IsOwnerOrReadOnly,)
# class SnippetHighlight(generics.GenericAPIView):
#     queryset = Snippets.objects.all()
#     renderer_classes = (renderers.StaticHTMLRenderer,)
#
#     def get(self,request,*args,**kwargs):
#         snippet = self.get_object()
#         return Response(snippet.highlighted)
#
# from django.contrib.auth.models import User
#
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# ViewSet
from rest_framework import viewsets
from django.contrib.auth.models import User

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework import permissions

class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippets.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)


    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self,request,*args,**kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)




@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })