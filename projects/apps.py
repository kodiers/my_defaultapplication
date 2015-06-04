#encoding=utf-8
# © Victor Yamchinov 2015.
# Projects application
# version 0.0.1a
from django.apps import AppConfig


class ProjectConfig(AppConfig):
    """
    Change application name to russian
    """
    name = 'projects'
    verbose_name = u"Управление проектами"
