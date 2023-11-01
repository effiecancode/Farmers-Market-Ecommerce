from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Profile


class RegistrationForm(UserCreationForm):

    # phone = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image", "bio"]

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image", "bio"]