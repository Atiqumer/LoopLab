# contact/forms.py
from django import forms
from .models import ContactSubmission

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'subject', 'message']
        
        # Use Tailwind-friendly widgets for attractive inputs
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-loop-accent focus:border-loop-accent transition duration-300', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-loop-accent focus:border-loop-accent transition duration-300', 'placeholder': 'Your Email'}),
            'subject': forms.TextInput(attrs={'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-loop-accent focus:border-loop-accent transition duration-300', 'placeholder': 'Subject of Inquiry'}),
            'message': forms.Textarea(attrs={'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-loop-accent focus:border-loop-accent transition duration-300', 'rows': 5, 'placeholder': 'Your Message'}),
        }