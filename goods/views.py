#encoding=utf-8
# © Victor Yamchinov 2015.
# Pages application
# version 0.0.1a

from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404
from django.views.generic import ListView, DetailView
from django.template import RequestContext
from django.core import serializers
from django.http import HttpResponse

from models import GoodsCategory, Goods

# Create your views here.

class CategoryGoodsList(ListView):
    """
    Show list of categories
    """
    model = GoodsCategory
    template_name = 'goods/category_list.html'


class GoodsList(ListView):
    """
    Show goods list
    """
    model = Goods
    template_name = 'goods/goods_list.html'


def related_goods(request):
    """
    Return list of goods sorted by category
    :param request:
    :return:
    """
    goods = Goods.objects.select_related('category').order_by('category')
    return render_to_response('goods/related_goods.html', {'goods': goods}, context_instance=RequestContext(request))

class GoodsDetailView(DetailView):
    """
    Show goods details
    """
    model = Goods
    template_name = 'goods/goods.html'


def json_one_good(request, pk):
    """
    Return one good as json
    :param request: request object
    :param pk: id of good
    :return: One good as JSON list
    """
    good = get_object_or_404(Goods, pk=pk)
    serialized_good = serializers.serialize('json', [good], fields=('pk', 'title', 'category', 'description',
                                                                    'created_date'))
    return HttpResponse(serialized_good, content_type='json')


def json_category(request, pk):
    """
    Return category as json
    :param request: request object
    :param pk: id of category
    :return: Return one category as JSON
    """
    category = get_object_or_404(GoodsCategory, pk=pk)
    serialized_category = serializers.serialize('json', [category], fields=('pk', 'title', 'created_date'))
    return HttpResponse(serialized_category, content_type='json')


def json_categories(request):
    """
    Return list of categories as JSON
    :param request: request object
    :return: Return list of categories as json
    """
    categories = get_list_or_404(GoodsCategory)
    serialized_categories = serializers.serialize('json', categories, fields=('pk', 'title', 'created_date'))
    return HttpResponse(serialized_categories, content_type='json')


def json_goods(request):
    """
    Return list of goods as json
    :param request: request object
    :return: List of goods as JSON
    """
    pages = get_list_or_404(Goods)
    serilized_goods = serializers.serialize('json', pages, fields=('pk', 'title', 'category', 'description',
                                                                   'created_date'))
    return HttpResponse(serilized_goods, content_type='json')


def json_goods_in_category(request, pk):
    """
    Return list of goods in category as json
    :param request: request object
    :param pk: id of category
    :return: List of goods in category as json
    """
    category = GoodsCategory.objects.get(pk=pk)
    goods = get_list_or_404(Goods, category=category)
    serialized_goods = serializers.serialize('json', goods, fields=('pk', 'title', 'category', 'description',
                                                                   'created_date'))
    return HttpResponse(serialized_goods, content_type='json')


