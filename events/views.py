# events/views.py

from django.shortcuts import render
from .models import Event 
from django.db.models import Q # Import Q objects for complex queries

def event_list(request):
    """Fetches, filters, and processes events to determine status and styling in Python."""
    
    event_filter = request.GET.get('filter', 'ALL')
    
    # Base Query: Order upcoming events first, then by date.
    events = Event.objects.all().order_by('-is_upcoming', 'date_time')
    
    if event_filter == 'UPCOMING':
        events = events.filter(is_upcoming=True)
    elif event_filter == 'PAST':
        events = events.filter(is_upcoming=False)

    # --- PROCESSING LOGIC: Add styling and text to each event object ---
    processed_events = []
    for event in events:
        if event.is_upcoming:
            event.status_bg = "bg-gradient-to-r from-loop-accent to-loop-indigo"
            event.status_text = "UPCOMING SESSION"
            event.link_text = "Register Now →"
        else:
            event.status_bg = "bg-gray-500"
            event.status_text = "EVENT COMPLETE"
            event.link_text = "View Summary →"
        processed_events.append(event)
    # ------------------------------------------------------------------
        
    context = {
        'events': processed_events,
        'page_title': 'Community Events & Webinars',
        'active_filter': event_filter 
    }
    
    # If it's an HTMX request, render only the cards partial
    if request.headers.get('hx-request'):
        return render(request, 'events/event_cards.html', context)
        
    # Otherwise, render the full page template
    return render(request, 'events/event_list.html', context)