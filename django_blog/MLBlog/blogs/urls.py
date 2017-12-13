from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'blogs',views.BlogsViewSet)
urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^blogs/new',views.newblog,name='blogs'),
    url(r'^blogs/(?P<pk>[0-9]+)/edit',views.edit,name='edit'),
    url(r'^blogs/(?P<pk>[0-9]+)',views.detail,name='detail'),
    url(r'^blogs/',views.blogs,name='blogs'),

               ]