from django.contrib import admin
from goods.models import GoodsCategory, Goods

# Register your models here.
from mce_filebrowser.admin import MCEFilebrowserAdmin      #for upload files through TinyMCE

# Register your models here.
class GoodsCategoryAdmin(MCEFilebrowserAdmin):
    """
    Admin class for GoodsCategory model
    """
    list_display = ('title',)
    search_fields = ('title',)


class GoodsAdmin(MCEFilebrowserAdmin):
    """
    Admin class for Goods model
    """
    list_display = ('title', 'category',)
    search_fields = ('title', 'description')
    list_filter = ('category',)


admin.site.register(GoodsCategory, GoodsCategoryAdmin)
admin.site.register(Goods, GoodsAdmin)