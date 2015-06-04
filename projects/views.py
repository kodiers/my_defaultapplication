#encoding=utf-8
# © Victor Yamchinov 2015.
# Projects application
# version 0.0.1a

from django.views.generic import ListView, DetailView

from models import Projects

# Create your views here.

class ProjectsList(ListView):
    """
    Show list of projects
    """
    model = Projects
    template_name = 'projects/projects_list.html'


class ProjectDetailView(DetailView):
    """
    Show projects details
    """
    model = Projects
    template_name = 'projects/projects.html'


