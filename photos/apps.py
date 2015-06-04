#encoding=utf-8
# © Victor Yamchinov 2015.
# Photos application
# version 0.0.1a
from django.apps import AppConfig


class PhotosConfig(AppConfig):
    """
    Change application name to russian
    """
    name = 'photos'
    verbose_name = u"Управление фотогалереей"