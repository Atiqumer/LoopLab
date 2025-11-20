# contact/views.py
from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponse # Required for HTMX POST response

def contact_view(request):
    """Handles displaying the form (GET) and asynchronous submission (POST)."""
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            # Save the submission to the database
            form.save()
            
            # HTMX Success Response: Swap the form out for a success message
            return render(request, 'contact/contact_success.html')
        else:
            # HTMX Error Response: Re-render the form with validation errors.
            # HTMX automatically swaps this content back into the original form container.
            return render(request, 'contact/contact_form.html', {'form': form})
            
    else:
        # Initial GET request
        form = ContactForm()
    
    # Render the full page template
    return render(request, 'contact/contact.html', {'form': form, 'page_title': 'Get In Touch'})