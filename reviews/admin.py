from django.contrib import admin
from reviews.models import Reviews

# Register your models here.
from mce_filebrowser.admin import MCEFilebrowserAdmin      #for upload files through TinyMCE

# Register your models here.


class ReviewsAdmin(MCEFilebrowserAdmin):
    """
    Admin class for Reviews model
    """
    list_display = ('name',)
    search_fields = ('name', 'text')
    readonly_fields = ('image_tag',)


admin.site.register(Reviews, ReviewsAdmin)
