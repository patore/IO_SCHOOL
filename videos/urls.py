from django.conf.urls import url
from .views import (
    VideoCreateView,
    VideoListView,
    VideoDetailView,
    VideoUpdateView,
    VideoDeleteView
)


urlpatterns = [
    url(r'^$', VideoListView.as_view(), name='list_video'),
    url(r'create_video/$', VideoCreateView.as_view(), name='create_video'),
    url(r'update_video/(?P<slug>[\w-]+)/$', VideoUpdateView.as_view(), name='update_video'),
    url(r'delete_video/(?P<slug>[\w-]+)/$', VideoDeleteView.as_view(), name='delete_video'),
    url(r'detail_video/(?P<slug>[\w-]+)/$', VideoDetailView.as_view(), name='detail_video')
]