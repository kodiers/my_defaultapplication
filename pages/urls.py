from django.conf.urls import include, url
# from django.contrib import admin
from pages.views import PageCategoryListView, PageListView, PageCategoryDetailView, PageDetailView, one_page_category, \
    many_page_category, json_one_page, json_category, json_category_pages, json_categories, json_pages, page_by_slug

urlpatterns = [
    url(r'^categories/', PageCategoryListView.as_view(), name='categories'),
    url(r'^pages/', PageListView.as_view(), name='pages'),
    url(r'^category/(?P<pk>\d+)/$', PageCategoryDetailView.as_view(), name='category'),
    url(r'^page/(?P<pk>\d+)/$', PageDetailView.as_view(), name='page'),
    url(r'^page/(?P<url>\w+)/$', page_by_slug, name='page_slug'),
    url(r'^page/(?P<category>\w+)/(?P<url>\w+)/$', one_page_category, name='one_page_category'),
    url(r'^pages/(?P<category>\w+)/$', many_page_category, name='many_page_category'),
    url(r'^json/pages/$', json_pages, name='json_pages'),
    url(r'^json/pages/(?P<url>\w+)/$', json_one_page, name='json_one_page'),
    url(r'^json/categories/$', json_categories, name='json_categories'),
    url(r'^json/categories/(?P<category>\w+)/$', json_category, name='json_category'),
    url(r'^json/pages/category/(?P<category>\w+)/$', json_category_pages, name='json_category_pages'),
    # url(r'^admin/', include(admin.site.urls)),
]