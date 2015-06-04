#encoding=utf-8
# © Victor Yamchinov 2015.
# Reviews application
# version 0.0.1a

from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.generic import ListView, DetailView
from django.core import serializers
from django.http import HttpResponse

from models import Partners

# Create your views here.

class PartnersList(ListView):
    """
    Show list of partners
    """
    model = Partners
    template_name = 'partners/partners_list.html'


class PartnerDetailView(DetailView):
    """
    Show partners details
    """
    model = Partners
    template_name = 'partners/partner.html'


def json_one_partner(request, pk):
    """
    Return one partner as json
    :param request: request object
    :param pk: id of partner
    :return: One partner as JSON list
    """
    partner = get_object_or_404(Partners, pk=pk)
    serialized_partner = serializers.serialize('json', [partner], fields=('pk', 'title', 'description', 'image', 'text',
                                                                        'created_date'))
    return HttpResponse(serialized_partner, content_type='json')


def json_partners(request):
    """
    Return list of partners as json
    :param request: request object
    :return: List of partners as JSON
    """
    partners = get_list_or_404(Partners)
    serilized_partners = serializers.serialize('json', partners, fields=('pk', 'title', 'description', 'image', 'text',
                                                                         'created_date'))
    return HttpResponse(serilized_partners, content_type='json')
