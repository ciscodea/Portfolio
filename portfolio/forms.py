""" Contact form """

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label=False, required=True, widget=forms.TextInput(attrs={'placeholder':'Name','class': 'form-control','required': True}))
    email = forms.EmailField(label=False, required=True, widget=forms.EmailInput(attrs={'placeholder':'Email','class': 'form-control','required': True}))
    message = forms.CharField(label=False, required=True, widget=forms.Textarea(attrs={'placeholder':'Message','class': 'form-control','required': True, 'rows':'4' }))
