#encoding=utf-8
# © Victor Yamchinov 2015.
# Pages application
# version 0.0.1a
from django.apps import AppConfig


class PartnersConfig(AppConfig):
    """
    Change application name to russian
    """
    name = 'partners'
    verbose_name = u"Управление разделом партнеры"
