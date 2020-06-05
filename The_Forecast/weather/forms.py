from django import forms
from .models import AddCity


class cityform(forms.Form):
	city_name = forms.CharField(widget=forms.TextInput(attrs={'size': '30'}),max_length=30, required=True)
    