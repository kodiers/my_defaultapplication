from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext

from models import PhotoCategory, PhotoImages

# Create your views here.

def related_photos(request):
    """
    Return list of images for project
    :param request: http request
    :return: HttpResponse
    """
    photos = PhotoImages.objects.select_related('category').order_by('category')
    return render_to_response('photos/photos_related.html', {'photos': photos}, context_instance=RequestContext(request))


def photo_by_category(request, pk):
    """
    Return list of images only for one category
    :param request: Request object
    :param pk: pk of category
    :return: HttpResponse object
    """
    category = get_object_or_404(PhotoCategory, pk=pk)
    photos = get_list_or_404(PhotoImages.objects.order_by('-show_on_list'), category=category)
    return render_to_response('photos/photos.html', {'category': category, 'photos': photos},
                              context_instance=RequestContext(request))


def show_list_true(request):
    """
    Return list of images, which have show_on_list = True
    :param request: request object
    :return: HttpResponse object
    """
    photos = get_list_or_404(PhotoImages, show_on_list=True)
    return render_to_response('photos/photos_list.html', {'photos': photos}, context_instance=RequestContext(request))