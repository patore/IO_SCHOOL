from django.conf.urls import url
from .views import (
    CategoriesCreateView,
    CategoriesListView,
    CategoriesDetailView,
    CategoriesUpdateView,
    CategoriesDeleteView
)


urlpatterns = [
    url(r'^$', CategoriesListView.as_view(), name='list_categories'),
    url(r'create_categories/$', CategoriesCreateView.as_view(), name='create_categories'),
    url(r'update_categories/(?P<slug>[\w-]+)/$', CategoriesUpdateView.as_view(), name='update_categories'),
    url(r'delete_categories/(?P<slug>[\w-]+)/$', CategoriesDeleteView.as_view(), name='delete_categories'),
    url(r'detail_categories/(?P<slug>[\w-]+)/$', CategoriesDetailView.as_view(), name='detail_categories')
    ]