from django.conf.urls import url
from .views import (
    CourseCreateView,
    CourseListView,
    CourseDetailView,
    CoursePurchaseView,
    CourseUpdateView,
    CourseDeleteView,
    LectureCreateView,
    LectureListView,
    LectureDetailView,
    LectureUpdateView,
    LectureDeleteView
)


urlpatterns = [
    url(r'^$', CourseListView.as_view(), name='list_course'),
    url(r'create_course/$', CourseCreateView.as_view(), name='create_course'),
    url(r'update_course/(?P<slug>[\w-]+)/$', CourseUpdateView.as_view(), name='update_course'),
    url(r'delete_course/(?P<slug>[\w-]+)/$', CourseDeleteView.as_view(), name='delete_course'),
    url(r'detail_course/(?P<slug>[\w-]+)/$', CourseDetailView.as_view(), name='detail_course'),
    url(r'purchase_course/(?P<slug>[\w-]+)/$', CoursePurchaseView.as_view(), name='purchase_course'),
    url(r'lectures/(?P<slug>[\w-]+)/$', LectureListView.as_view(), name='list_lecture'),
    url(r'create_lecture/$', LectureCreateView.as_view(), name='create_lecture'),
    url(r'update_lecture/(?P<slug>[\w-]+)/$', LectureUpdateView.as_view(), name='update_lecture'),
    url(r'delete_lecture/(?P<slug>[\w-]+)/$', LectureDeleteView.as_view(), name='delete_lecture'),
    url(r'detail_lecture/(?P<slug>[\w-]+)/$', LectureDetailView.as_view(), name='detail_lecture')
]