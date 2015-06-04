#encoding=utf-8
# © Victor Yamchinov 2015.
# CEO application
# version 0.0.1a
from django import template
from ceo.models import CEO

register = template.Library()


@register.simple_tag()
def keywords():
    """
    :return: keywords
    """
    ceo = CEO.objects.get(pk=1)
    return ceo.keywords


@register.simple_tag()
def description():
    """
    :return: description
    """
    ceo = CEO.objects.get(pk=1)
    return ceo.description
