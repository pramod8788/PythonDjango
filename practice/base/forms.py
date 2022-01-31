from django import forms
from . import models

class InfoForm(forms.ModelForm):
    class Meta:
        model = models.info
        fields = "__all__"