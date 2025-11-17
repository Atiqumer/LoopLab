# backend/projects/views.py

from django.shortcuts import render
from .models import Project 

def project_list(request):
    """Fetches all projects and renders the list page."""
    projects = Project.objects.all().order_by('-date_created')
    
    context = {
        'projects': projects,
        'page_title': 'Community Projects Showcase'
    }
    
    return render(request, 'projects/project_list.html', context)