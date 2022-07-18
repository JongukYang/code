from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(label='Search Movies', max_length=100)
