#encoding=utf-8
# © Victor Yamchinov 2015.
# Goods application
# version 0.0.1a


from django.db import models
from tinymce.models import HTMLField
from django.utils import timezone

# Create your models here.

class GoodsCategory(models.Model):
    """
    Goods category class
    """
    title = models.TextField(verbose_name=u"Название категории")
    created_date = models.DateField(default=timezone.now, verbose_name=u"Дата создания")

    @property
    def serialize(self):
        """
        Property for return fields as dictionary
        :return dictionary object
        """
        return {
            'id': self.pk,
            'title': self.title,
            'created_date': self.created_date
        }

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        ordering = ['pk']
        verbose_name = u"Категория услуг"
        verbose_name_plural = u"Категории услуг"


class Goods(models.Model):
    """
    Goods class
    """
    title = models.TextField(verbose_name=u"Название услуги")
    category = models.ForeignKey(GoodsCategory, verbose_name=u"Категория")
    description = HTMLField(verbose_name=u"Описание услуги", null=True, blank=True)
    created_date = models.DateField(default=timezone.now, verbose_name=u"Дата создания")

    @property
    def serialize(self):
        """
        Property for return fields as dictionary
        :return dictionary object
        """
        return {
            'id': self.pk,
            'title': self.title,
            'category': self.category.title,
            'description': self.description,
            'created_date': self.created_date
        }

    def __unicode__(self):
        return u'%s' % self.title

    def get_absolute_url(self):
        return ("/good/%i" % self.pk)

    class Meta:
        ordering = ['pk']
        verbose_name = u"Услуга"
        verbose_name_plural = u"Услуги"




