from django.contrib import admin
from ceo.models import CEO

# Register your models here.
class CEOAdmin(admin.ModelAdmin):
    """
    Admin class for CEO model
    """
    search_fields = ('keywords', 'description', )

    def get_actions(self, request):
        actions = super(CEOAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(CEO, CEOAdmin)
