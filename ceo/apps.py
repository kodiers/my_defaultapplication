#encoding=utf-8
# © Victor Yamchinov 2015.
# CEO application
# version 0.0.1a
from django.apps import AppConfig


class CEOConfig(AppConfig):
    """
    Change application name to russian
    """
    name = 'ceo'
    verbose_name = u"Управление ключевыми словами и описанием"
