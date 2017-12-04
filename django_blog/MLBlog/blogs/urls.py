from django.conf.urls import url, include
from rest_framework import routers
import views

router = routers.DefaultRouter()
router.register(r'blog',views.BlogsViewSet)
urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^login/',views.login,name='login'),
    url(r'^blogs/(?P<pk>[0-9]+)/$',views.detail,name='detail'),
    url(r'^blogs/',views.blogs,name='blogs'),

               ]