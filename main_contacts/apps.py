#encoding=utf-8
# © Victor Yamchinov 2015.
# Main_contacts application
# version 0.0.1a
from django.apps import AppConfig


class MainContactsConfig(AppConfig):
    """
    Change application name to russian
    """
    name = 'main_contacts'
    verbose_name = u"Управление главной страницей и контактами"
