from django import forms
from .models import *

class ChoiceFrom(forms.ModelForm):
    class Meta:
        model = Buy
        exclude = ['product']
        fields = '__all__'


class RegisterUp(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Register
        fields = '__all__'
        exclude = ['message']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        exclude = ['password', 'phone', 'last_name']
