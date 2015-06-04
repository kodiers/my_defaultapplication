#encoding=utf-8
# © Victor Yamchinov 2015.
# Pages application
# version 0.0.1a


from django.db import models
from tinymce.models import HTMLField
from django.utils import timezone

# Create your models here.

class Reviews(models.Model):
    """
    Reviews class
    """
    name = models.TextField(verbose_name=u"Имя")
    image = models.ImageField(verbose_name=u"Изображение", null=True, blank=True, upload_to='images')
    text = HTMLField(verbose_name=u"Текст отзыва", null=True, blank=True)
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
            'name': self.name,
            'image': self.image.url,
            'text': self.text,
            'created_date': self.created_date
        }

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        ordering = ['created_date']
        verbose_name = u"Отзыв"
        verbose_name_plural = u"Отзывы"
