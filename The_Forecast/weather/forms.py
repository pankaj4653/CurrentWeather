from django import forms
from .models import AddCity


class cityform(forms.ModelForm):
    cityName = forms.CharField(widget=forms.TextInput(attrs={'size': '30'}),max_length=30, required=True)
    class Meta:
        model = AddCity
        fields = '__all__'