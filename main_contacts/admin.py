from django.contrib import admin
from main_contacts.models import MainPageText, Advantages, Contacts

from mce_filebrowser.admin import MCEFilebrowserAdmin      #for upload files through TinyMCE

# Register your models here.
class MainPageTextAdmin(MCEFilebrowserAdmin):
    """
    Admin class for MainPageText model
    """
    readonly_fields = ('image_tag',)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super(MainPageTextAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


class AdvantagesAdmin(MCEFilebrowserAdmin):
    """
    Admin class for Advantages model
    """
    list_display = ('title',)
    search_fields = ('title', 'text')
    readonly_fields = ('image_tag',)


class ContactsAdmin(MCEFilebrowserAdmin):
    """
    Admin class for contacts model
    """

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super(ContactsAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


admin.site.register(MainPageText, MainPageTextAdmin)
admin.site.register(Advantages, AdvantagesAdmin)
admin.site.register(Contacts, ContactsAdmin)
