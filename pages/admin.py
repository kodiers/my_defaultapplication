#encoding=utf-8
# © Victor Yamchinov 2015.
# Pages application
# version 0.0.1a

from django.contrib import admin
from pages.models import PageCategory, Pages
from mce_filebrowser.admin import MCEFilebrowserAdmin      #for upload files through TinyMCE

# Register your models here.
class PageCategoryAdmin(MCEFilebrowserAdmin):
    """
    Admin class for PagesCategory model
    """
    list_display = ('title',)
    search_fields = ('title', 'content')


class PagesAdmin(MCEFilebrowserAdmin):
    """
    Admin class for Pages model
    """
    list_display = ('title', 'category', 'modified_date')
    search_fields = ('title', 'content')
    list_filter = ('category', 'modified_date')


admin.site.register(PageCategory, PageCategoryAdmin)
admin.site.register(Pages, PagesAdmin)