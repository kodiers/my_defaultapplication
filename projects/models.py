#encoding=utf-8
# © Victor Yamchinov 2015.
# Projects application
# version 0.0.1a


from django.db import models
from tinymce.models import HTMLField
from django.utils import timezone

# Create your models here.

class Projects(models.Model):
    """
    Reviews class
    """
    title = models.TextField(verbose_name=u"Название")
    image = models.ImageField(verbose_name=u"Изображение", null=True, blank=True, upload_to='images')
    text = HTMLField(verbose_name=u"Описание", null=True, blank=True)
    created_date = models.DateField(default=timezone.now, verbose_name=u"Дата")

    def image_tag(self):
        return u'<img src="%s" height=75 width=75 />' % (self.image.url)

    image_tag.short_description = u"Текущee изображение"
    image_tag.allow_tags = True

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        ordering = ['created_date']
        verbose_name = u"Проект"
        verbose_name_plural = u"Проекты"