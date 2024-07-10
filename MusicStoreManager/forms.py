from django import forms
from .models import MelodiesToLearn

class MelodiesToLearnForm(forms.ModelForm):
    class Meta:
        model = MelodiesToLearn
        fields = ['name', 'style']

