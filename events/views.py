# backend/events/views.py

from django.shortcuts import render
from .models import Event 

def event_list(request):
    """Fetches all events, sorted by date."""
    # Fetch events, sorting upcoming first, then by date.
    events = Event.objects.all().order_by('-is_upcoming', 'date_time')
    
    context = {
        'events': events,
        'page_title': 'Community Events & Webinars'
    }
    
    return render(request, 'events/event_list.html', context)