# backend/events/models.py

from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(help_text="Full description of the event.")
    
    # Event details
    date_time = models.DateTimeField(help_text="The start date and time of the event.")
    location = models.CharField(max_length=150, help_text="Physical address or online meeting link.")
    
    # Required visual element (banner/image)
    banner_url = models.URLField(
        blank=True, 
        null=True, 
        help_text="Link to a placeholder image or event banner."
    )
    
    # Status to easily separate upcoming from past events
    is_upcoming = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ['date_time'] # Default ordering by date