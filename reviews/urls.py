from django.conf.urls import include, url
from django.contrib import admin
from reviews.views import ReviewDetailView, ReviewsList, json_one_review, json_reviews

urlpatterns = [
    url(r'^reviews/$', ReviewsList.as_view(), name='reviews'),
    url(r'^review/(?P<pk>\d+)/$', ReviewDetailView.as_view(), name='review'),
    url(r'^json/review/(?P<pk>\d+)/$', json_one_review, name='json_review'),
    url(r'^json/reviews/$', json_reviews, name='json_reviews'),
    # url(r'^admin/', include(admin.site.urls)),
]
