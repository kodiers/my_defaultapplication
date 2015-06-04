from django.contrib import admin
from projects.models import Projects

# Register your models here.
from mce_filebrowser.admin import MCEFilebrowserAdmin      #for upload files through TinyMCE

# Register your models here.


class ProjectsAdmin(MCEFilebrowserAdmin):
    """
    Admin class for Projects model
    """
    list_display = ('title',)
    search_fields = ('title', 'text')
    readonly_fields = ('image_tag',)


admin.site.register(Projects, ProjectsAdmin)

