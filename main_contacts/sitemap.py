#encoding=utf-8
# © Victor Yamchinov 2015.
# version 0.0.1a
from goods.models import Goods
from main_contacts.models import MainPageText
from pages.models import Pages

from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse


class GoodsSitemap(Sitemap):
    changefreq = 'monthly'

    def items(self):
        return Goods.objects.all()


class PagesSitemap(Sitemap):
    changefreq = "monthly"

    def items(self):
        return Pages.objects.all()


class StaticSitemap(Sitemap):
    changefreq = "monthly"

    def items(self):
        return ['index', 'contacts', 'partners', 'reviews']

    def location(self, obj):
        return reverse(obj)


sitemaps = {
    'static': StaticSitemap,
    u"Страницы сайта": PagesSitemap,
    u"Услуги": GoodsSitemap
}