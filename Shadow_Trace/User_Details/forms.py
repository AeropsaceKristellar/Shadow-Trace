# forms.py
from django import forms
from . models import User

class ContactForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["User_Name", 'firstName', 'lastName', 'emailId', 'z']