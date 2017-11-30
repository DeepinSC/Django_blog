from django.conf.urls import url, include
from rest_framework import routers
import views

router = routers.DefaultRouter()
router.register(r'blogs',views.BlogsViewSet)
urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^index/',views.index,name='index'),
    url(r'^login/',views.login,name='login'),
               ]