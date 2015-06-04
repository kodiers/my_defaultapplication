#encoding=utf-8
# © Victor Yamchinov 2015.
# Main_contacts application
# version 0.0.1a

from django.db import models

# Create your models here.

class CEO(models.Model):
    """
    Model for keywords and description
    """
    description = models.CharField(max_length=256, verbose_name='META DESCRIPTION')
    keywords = models.TextField(verbose_name='META KEYWORDS')

    def __unicode__(self):
        return u'%s' % self.description

    class Meta:
        verbose_name_plural = u"Ключевые слова и описание"
