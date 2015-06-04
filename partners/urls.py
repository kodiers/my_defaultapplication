from django.conf.urls import include, url
from django.contrib import admin
from partners.views import PartnersList, PartnerDetailView, json_one_partner, json_partners

urlpatterns = [
    url(r'^partners/$', PartnersList.as_view(), name='partners'),
    url(r'^partner/(?P<pk>\d+)/$', PartnerDetailView.as_view(), name='partner'),
    url(r'^json/partner/(?P<pk>\d+)/$', json_one_partner, name='json_partner'),
    url(r'^json/reviews/$', json_partners, name='json_partners'),
    # url(r'^admin/', include(admin.site.urls)),
]

