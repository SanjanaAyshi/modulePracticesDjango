from django import forms
from .models import Musicians


class MusiciansFrom(forms.ModelForm):
    class Meta:
        model = Musicians
        fields = '__all__'
