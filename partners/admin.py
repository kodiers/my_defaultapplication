from django.contrib import admin
from partners.models import Partners

# Register your models here.
from mce_filebrowser.admin import MCEFilebrowserAdmin      #for upload files through TinyMCE

# Register your models here.


class PartnersAdmin(MCEFilebrowserAdmin):
    """
    Admin class for Partners model
    """
    list_display = ('title',)
    search_fields = ('title', 'text', 'description')
    readonly_fields = ('image_tag',)


admin.site.register(Partners, PartnersAdmin)