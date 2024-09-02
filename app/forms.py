from django import forms
from app.models import *

class homepageform(forms.ModelForm):
    class Meta:
        model=Flights
        fields='__all__'