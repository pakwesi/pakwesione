# sendemail/forms.py
from django import forms
from .models import contact_us

class Contact_usForm(forms.ModelForm):
    naam = forms.CharField(label='naam', widget=forms.TextInput(attrs={'class': 'special'}))
    class Meta:
        model = contact_us
        fields = ['naam', 'email', 'onderwerp', 'bericht']
