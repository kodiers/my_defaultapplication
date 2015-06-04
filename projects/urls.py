__author__ = 'kodiers'
from django.conf.urls import include, url
from django.contrib import admin
from projects.views import ProjectsList, ProjectDetailView

urlpatterns = [
    url(r'^projects/$',ProjectsList.as_view(), name='projects'),
    url(r'^project/(?P<pk>\d+)/$', ProjectDetailView.as_view(), name='project'),
    # url(r'^admin/', include(admin.site.urls)),
]