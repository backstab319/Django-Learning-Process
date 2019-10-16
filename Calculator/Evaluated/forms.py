from django import forms

class CalForm(forms.Form):
    expr = forms.CharField()