#encoding=utf-8
# © Victor Yamchinov 2015.
# Goods application
# version 0.0.1a
from django.apps import AppConfig


class GoodsConfig(AppConfig):
    """
    Change application name to russian
    """
    name = 'goods'
    verbose_name = u"Управление услугами"
