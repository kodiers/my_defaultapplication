#encoding=utf-8
# © Victor Yamchinov 2015.
# Photos application
# version 0.0.1a

from django.db import models
from django.utils import timezone

# Create your models here.

class PhotoCategory(models.Model):
    """
    Model for photo category
    """
    title = models.TextField(verbose_name=u"Название проекта")
    description = models.TextField(verbose_name=u"Описание проекта", null=True, blank=True)
    date = models.DateField(default=timezone.now, verbose_name=u"Дата")

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        ordering = ['pk']
        verbose_name = u"Проект"
        verbose_name_plural = u"Проекты"


class PhotoImages(models.Model):
    """
    Images model for photo
    """
    title = models.TextField(verbose_name=u"Название")
    category = models.ForeignKey(PhotoCategory, verbose_name=u"Проект")
    date = models.DateField(default=timezone.now, verbose_name=u"Дата")
    image = models.ImageField(upload_to='images', verbose_name=u"Изображение")
    show_on_list = models.BooleanField(default=False, verbose_name=u"Показывать в списке проектов")

    def image_tag(self):
        return u'<img src="%s" height=75 width=75 />' % (self.image.url)

    image_tag.short_description = u"Текущее изображение"
    image_tag.allow_tags = True

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        ordering=['pk']
        verbose_name = u"Фотография"
        verbose_name_plural = u"Фотографии"