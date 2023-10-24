from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegistrationForm(UserCreationForm):

    phone = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password1', 'password2']