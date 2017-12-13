from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SnippetViewSet,UserViewSet,api_root
from django.conf.urls import include
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

# snippet_list = SnippetViewSet.as_view({
#     'get':'list',
#     'post':'create'
# })
#
# snippet_detail = SnippetViewSet.as_view({
#     'get':'retrieve',
#     'put':'update',
#     'patch':'partial_update',
#     'delete':'destory'
# })
#
# snippet_highlight = SnippetViewSet.as_view({
#     'get':'highlight'
# },renderer_classes=[renderers.StaticHTMLRenderer])
#
# user_list = UserViewSet.as_view({
#     'get':'list'
# })
#
# user_detail = UserViewSet.as_view({
#     'get':'retrieve'
# })
#
# # API endpoints
# urlpatterns = format_suffix_patterns([
#     url(r'^$', views.api_root),
#     url(r'^snippets/$',
#         snippet_list,
#         name='snippet-list'),
#     url(r'^snippets/(?P<pk>[0-9]+)/$',
#         snippet_detail,
#         name='snippets-detail'),
#     url(r'^snippets/(?P<pk>[0-9]+)/highlight/$',
#         snippet_highlight,
#         name='snippet-highlight'),
#     url(r'^users/$',
#         user_list,
#         name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$',
#         user_detail,
#         name='user-detail')
# ])
#
# # Login and logout views for the browsable API
# urlpatterns += [
#     url(r'^api-auth/', include('rest_framework.urls',
#                                namespace='rest_framework')),
# ]

router = DefaultRouter()
router.register(r'snippets',views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]