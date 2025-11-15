# Create your views here.
# members/views.py
from django.shortcuts import render
from .models import Contributor # Import the model

def contributor_list(request):
    """Fetches all contributors and sends them to the template."""
    # Query the database to get all contributor objects
    contributors = Contributor.objects.all()

    # Prepare the context dictionary to pass data to the template
    context = {
        'contributors': contributors,
        'page_title': 'LoopLab Contributors'
    }

    # Renderig the template
    return render(request, 'members/contributor_list.html', context)