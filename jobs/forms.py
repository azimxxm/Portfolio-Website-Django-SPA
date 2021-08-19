from django import forms
from django.forms import fields
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['firstName', 'lastName', 'phoneNumber', 'email', 'message']