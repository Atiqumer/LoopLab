from django.shortcuts import render

# Create your views here.
# pages/views.py

from django.shortcuts import render

def home_page(request):
    """View for the Home/About page."""
    return render(request, 'pages/home.html', {
        'page_title': 'Home | LoopLab Community'
    })