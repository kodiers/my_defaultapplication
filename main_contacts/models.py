#encoding=utf-8
# © Victor Yamchinov 2015.
# Main_contacts application
# version 0.0.1a

from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class MainPageText(models.Model):
    """
    Main page block texts and image
    """
    losung = models.TextField(verbose_name=u"Текст на изображении(лозунг)", null=True, blank=True)
    image_text = models.TextField(verbose_name=u"Комментарий к лозунгу", null=True, blank=True)
    about_company = HTMLField(verbose_name=u"Текст о компании")
    image = models.ImageField(upload_to='images', null=True, blank=True, verbose_name=u"Изображение")

    def image_tag(self):
        return u'<img src="%s" height=75 width=75 />' % (self.image.url)

    image_tag.short_description = u"Текущее фото"
    image_tag.allow_tags = True

    @property
    def serialize(self):
        return {
            'losung': self.losung,
            'image_text': self.image_text,
            'about_company': self.about_company,
            'image': self.image.url,
        }

    def __unicode__(self):
        return u"Главная страница"

    class Meta:
        verbose_name = u"Главная"
        verbose_name_plural = verbose_name


class Advantages(models.Model):
    """
    Advantages model
    """
    title = models.CharField(max_length=256, verbose_name=u"Название")
    text = HTMLField(verbose_name=u"Описание")
    image = models.ImageField(upload_to='images', null=True, blank=True, verbose_name=u"Изображение")

    def image_tag(self):
        return u'<img src="%s" height=75 width=75 />' % (self.image.url)

    image_tag.short_description = u"Текущее фото"
    image_tag.allow_tags = True

    @property
    def serialize(self):
        return {
            'id': self.pk,
            'title': self.title,
            'text': self.text,
            'image': self.image.url
        }

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        verbose_name = u"Преимущество"
        verbose_name_plural = u"Преимущества"


class Contacts(models.Model):
    """
    Contacts class
    """
    phone = models.CharField(max_length=128, verbose_name=u"Телефон")
    phone_2 = models.CharField(max_length=128, verbose_name=u"Дополнительный телефон", null=True, blank=True)
    zip = models.CharField(max_length=128, verbose_name=u"Почтовый индекс")
    address = models.TextField(verbose_name=u"Адрес")
    email = models.EmailField(default='test@test.ru')
    businessdays = models.CharField(max_length=256, null=True, blank=True, verbose_name=u"Режим работы")
    map = models.CharField(max_length=256, blank=True, null=True, verbose_name=u"Скрипт карты")
    comments = HTMLField(null=True, blank=True, verbose_name=u"Комментарии")

    @property
    def serialize(self):
        return {
            'phone': self.phone,
            'phone_2': self.phone_2,
            'zip': self.zip,
            'address': self.address,
            'email': self.email,
            'map': self.map,
            'comments': self.comments
        }

    def __unicode__(self):
        return u'Контакты'

    class Meta:
        verbose_name_plural = u"Контакты"
