#encoding=utf-8
# © Victor Yamchinov 2015.
# Reviews application
# version 0.0.1a

from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.generic import ListView, DetailView
from django.core import serializers
from django.http import HttpResponse

from models import Reviews

# Create your views here.

class ReviewsList(ListView):
    """
    Show list of reviews
    """
    model = Reviews
    template_name = 'reviews/reviews_list.html'


class ReviewDetailView(DetailView):
    """
    Show goods details
    """
    model = Reviews
    template_name = 'reviews/review.html'


def json_one_review(request, pk):
    """
    Return one review as json
    :param request: request object
    :param pk: id of review
    :return: One good as JSON list
    """
    review = get_object_or_404(Reviews, pk=pk)
    serialized_review = serializers.serialize('json', [review], fields=('pk', 'name', 'image', 'text', 'created_date'))
    return HttpResponse(serialized_review, content_type='json')


def json_reviews(request):
    """
    Return list of goods as json
    :param request: request object
    :return: List of goods as JSON
    """
    reviews = get_list_or_404(Reviews)
    serilized_reviews = serializers.serialize('json', reviews, fields=('pk', 'name', 'image', 'text', 'created_date'))
    return HttpResponse(serilized_reviews, content_type='json')

