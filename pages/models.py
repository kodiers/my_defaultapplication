#encoding=utf-8
# © Victor Yamchinov 2015.
# Pages application
# version 0.0.1a

from django.db import models
from tinymce.models import HTMLField
from django.utils import timezone

# Create your models here.


class PageCategory(models.Model):
    """
    Page category class
    """
    title = models.TextField(verbose_name=u"Название")
    category_id = models.CharField(max_length=128, verbose_name=u"ID")
    content = HTMLField(verbose_name=u"Описание", null=True, blank=True)
    created_date = models.DateTimeField(verbose_name=u"Дата создания", default=timezone.now)

    @property
    def serialize(self):
        """
        Property for return fields as dictionary
        :return dictionary object
        """
        return {
            'pk': self.pk,
            'title': self.title,
            'category_id': self.category_id,
            'content': self.content,
            'created_date': self.created_date
        }

    def __unicode__(self):
        """
        Return name of models as unicode
        """
        return u'%s' % self.title

    class Meta:
        verbose_name = u"Категория страниц"
        verbose_name_plural = u"Категории страниц"
        ordering = ['created_date']


class Pages(models.Model):
    """
    Pages class
    """
    title = models.TextField(verbose_name=u"Заголовок")
    url = models.SlugField(verbose_name=u"URL")
    category = models.ForeignKey(PageCategory, null=True, blank=True, verbose_name=u"Категория")
    content = HTMLField(verbose_name=u"Текст")
    created_date = models.DateTimeField(auto_now=True, verbose_name=u"Дата создания")
    modified_date = models.DateTimeField(default=timezone.now, verbose_name=u"Дата изменения")

    @property
    def serialize(self):
        """
        Property for return fields as dictionary
        :return dictionary object
        """
        return {
            'pk': self.pk,
            'title': self.title,
            'url': self.url,
            'category': self.category.title,
            'content': self.content,
            'created_date': self.created_date,
            'modified_date': self.modified_date
        }

    def get_absolute_url(self):
        return '/page/page/' + str(self.pk)

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        verbose_name = u"Страница сайта"
        verbose_name_plural = u"Страницы сайта"
        ordering = ['modified_date']