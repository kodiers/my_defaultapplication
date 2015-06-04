from django.conf.urls import include, url
# from django.contrib import admin
from main_contacts.views import index, contacts, json_contacts

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^contacts/$', contacts, name='contacts'),
    url(r'^json/contacts/$', json_contacts, name='json_contacts'),
    # url(r'^admin/', include(admin.site.urls)),
]
