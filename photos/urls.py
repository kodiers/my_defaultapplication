__author__ = 'kodiers'
from django.conf.urls import include, url

from views import related_photos, photo_by_category, show_list_true

urlpatterns = [
    url(r'^related_photos/$', related_photos, name='related_photos'),
    url(r'^photos/$', show_list_true, name='photos'),
    url(r'^photo/(?P<pk>\d+)/$', photo_by_category, name='photo'),
]
