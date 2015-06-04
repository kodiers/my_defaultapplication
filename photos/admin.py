from django.contrib import admin
from models import PhotoCategory, PhotoImages

# Register your models here.

class PhotoCategoryAdmin(admin.ModelAdmin):
    """
    Admin model for Photo category
    """
    list_display = ('title', 'date')
    search_fields = ('title', 'description')
    list_filter = ('date',)


class PhotoImagesAdmin(admin.ModelAdmin):
    """
    Admin model for Photo images
    """
    list_display = ('title', 'category', 'date', 'show_on_list')
    search_fields = ('title', 'category')
    list_filter = ('category', 'date', 'show_on_list')
    readonly_fields = ('image_tag',)


admin.site.register(PhotoCategory, PhotoCategoryAdmin)
admin.site.register(PhotoImages, PhotoImagesAdmin)