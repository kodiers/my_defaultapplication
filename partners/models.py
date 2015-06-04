#encoding=utf-8
# © Victor Yamchinov 2015.
# Pages application
# version 0.0.1a


from django.db import models
from tinymce.models import HTMLField
from django.utils import timezone

# Create your models here.

class Partners(models.Model):
    """
    Partners class
    """
    title = models.TextField(verbose_name=u"Название")
    image = models.ImageField(verbose_name=u"Логотип", null=True, blank=True, upload_to='images')
    description = models.TextField(verbose_name=u"Описание", null=True, blank=True)
    text = HTMLField(verbose_name=u"Полное описание", null=True, blank=True)
    created_date = models.DateField(default=timezone.now, verbose_name=u"Дата")

    def image_tag(self):
        return u'<img src="%s" height=75 width=75 />' % (self.image.url)
    image_tag.short_description = u"Текущee изображение"
    image_tag.allow_tags = True

    @property
    def serialize(self):
        """
        Property for return fields as dictionary
        :return dictionary object
        """
        return {
            'id': self.pk,
            'name': self.title,
            'image': self.image.url,
            'description': self.description,
            'text': self.text,
            'created_date': self.created_date
        }

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        ordering = ['created_date']
        verbose_name = u"Партнер"
        verbose_name_plural = u"Партнеры"
