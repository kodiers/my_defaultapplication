#encoding=utf-8
# © Victor Yamchinov 2015.
# Pages application
# version 0.0.1a
from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404
from pages.models import PageCategory, Pages
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.template import RequestContext
from django.http import Http404, HttpResponse
from django.core import serializers

# Create your views here.


class PageCategoryListView(ListView):
    """
    List all categories
    """
    template_name = 'pages/category_list.html'
    model = PageCategory


class PageListView(ListView):
    """
    List all pages
    """
    template_name = 'pages/page_list.html'
    model = Pages


class PageCategoryDetailView(DetailView):
    """
    Show one category
    """
    template_name = 'pages/category.html'
    model = PageCategory


class PageDetailView(DetailView):
    """
    Show one page
    """
    template_name = 'pages/page.html'
    model = Pages


def page_by_slug(request, url):
    """
    Show page by slug field
    :param request:
    :param url:
    :return:
    """
    page = get_object_or_404(Pages, url=url)
    return render_to_response('pages/page.html', {'object': page}, context_instance=RequestContext(request))

def one_page_category(request, category, url):
    """
    Show one page in category
    :param request: request object
    :param category: category_id
    :param url: slug of page
    :return: HttpResponse objec as one page
    """
    pagecategory = get_object_or_404(PageCategory, category_id=category)
    try:
        page = Pages.objects.get(Q(category=pagecategory) & Q(url=url))
    except Pages.DoesNotExist, Pages.MultipleObjectsReturned:
        raise Http404("Page does not exist")
    return render_to_response('pages/page.html', {'object': page}, context_instance=RequestContext(request))


def many_page_category(request, category):
    """
    Show all pages in category
    :param request: request object
    :param category: category id
    :return: HttpResponse object as list of pages in category
    """
    pagecategory = get_object_or_404(PageCategory, category_id=category)
    pages = get_list_or_404(Pages, category=pagecategory)
    return render_to_response('pages/page_list.html', {'object_list': pages}, context_instance=RequestContext(request))


def json_one_page(request, url):
    """
    Return one page as json
    :param request: request object
    :return: Return one page as JSON
    """
    page = get_object_or_404(Pages, url=url)
    serialized_page = serializers.serialize('json', [page], fields=('pk', 'title', 'url', 'category', 'content',
                                                                    'created_date', 'modified_date'))
    return HttpResponse(serialized_page, content_type='json')


def json_category(request, category):
    """
    Return one category as JSON
    :param request: http request object
    :param category: category_id
    :return: Return on category as JSON
    """
    category = get_object_or_404(PageCategory, category_id=category)
    serialized_category = serializers.serialize('json', [category], fields=('pk', 'title', 'content', 'category_id',
                                                                            'created_date'))
    return HttpResponse(serialized_category, content_type='json')


def json_category_pages(request, category):
    """
    Return list of pages in category as JSON
    :param request: httprequest object
    :param category: category_id
    :return: list of pages in category as JSON
    """
    category = get_object_or_404(PageCategory, category_id=category)
    pages = get_list_or_404(Pages, category=category)
    serialized_pages = serializers.serialize('json', pages, fields=('pk', 'title', 'url', 'category', 'content',
                                                                    'created_date', 'modified_date'))
    return HttpResponse(serialized_pages, content_type='json')


def json_categories(request):
    """
    Return list of categories as json
    :param request: httprequest object
    :return: list of categories as json
    """
    categories = get_list_or_404(PageCategory)
    serialized_categories = serializers.serialize('json', categories, fields=('pk', 'title', 'content', 'category_id',
                                                                              'created_date'))
    return HttpResponse(serialized_categories, content_type='json')


def json_pages(request):
    """
    Return list of pages as JSON
    :param request: httprequest object
    :return: list of pages as json
    """
    pages = get_list_or_404(Pages)
    serilized_pages = serializers.serialize('json', pages, fields=('pk', 'title', 'url', 'category', 'content',
                                                                   'created_date', 'modified_date'))
    return HttpResponse(serilized_pages, content_type='json')




