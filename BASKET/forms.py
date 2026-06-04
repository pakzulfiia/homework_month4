from django import forms
from . import models

class ThingForm(forms.ModelForm):
    class Meta:
        model = models.Thing
        fields = '__all__'