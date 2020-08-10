from django import forms

from todoapp.models import List

class ListForm(forms.ModelForm):

    class Meta:
        model = List
        fields = ['task']
