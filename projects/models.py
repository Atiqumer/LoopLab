
# Create your models here.
# backend/projects/models.py

from django.db import models
# Import the Contributor model from the members app to create the link
from members.models import Contributor 

class Project(models.Model):
    title = models.CharField(max_length=200)
    tagline = models.CharField(max_length=250, blank=True, help_text="A short, catchy summary of the project.")
    description = models.TextField()
    
    # A project can have multiple contributors, and a contributor can work on multiple projects (Many-to-Many)
    contributors = models.ManyToManyField(
        Contributor, 
        related_name='contributed_projects', 
        blank=True
    )
    
    # URL for the live site or GitHub repository
    live_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    
    # Use a choice field to categorize the project (for future filtering/HTMX features)
    CATEGORY_CHOICES = [
        ('FRONTEND', 'Frontend'),
        ('BACKEND', 'Backend'),
        ('FULLSTACK', 'Full Stack'),
        ('DESIGN', 'Design'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='FULLSTACK')
    
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title