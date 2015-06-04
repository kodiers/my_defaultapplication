from django.conf.urls import include, url
# from django.contrib import admin
from goods.views import CategoryGoodsList, GoodsList, related_goods, GoodsDetailView, json_one_good, json_category, \
    json_categories, json_goods, json_goods_in_category

urlpatterns = [
    url(r'^categories/$', CategoryGoodsList.as_view(), name='goods_categoris'),
    url(r'^goods/$', GoodsList.as_view(), name='goods_list'),
    url(r'^related-goods/$', related_goods, name='related_goods'),
    url(r'^good/(?P<pk>\d+)/$', GoodsDetailView.as_view(), name='good'),
    url(r'^json/good/(?P<pk>\d+)/$', json_one_good, name='json_good'),
    url(r'^json/category/(?P<pk>\d+)/$', json_category, name='json_category'),
    url(r'^json/categories/$', json_categories, name='json_categories'),
    url(r'^json/goods/$', json_goods, name='json_goods'),
    url(r'^json/goods-in-category/(?P<pk>\d+)/$', json_goods_in_category, name='json_goods_in_category'),
    # url(r'^admin/', include(admin.site.urls)),
]