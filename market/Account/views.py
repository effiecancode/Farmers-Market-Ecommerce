from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Profile
from .forms import RegistrationForm, ProfileForm, UpdateProfileForm

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully', extra_tags="success")
            return redirect('Account:signin')
        else:
            messages.error(request, 'Unsuccessful Registration', extra_tags="error")

    form = RegistrationForm()
    return render(request, 'Account/signup.html', {'form':form})

