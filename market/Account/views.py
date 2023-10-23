from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import RegistrationForm

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('Account:home')
        else:
            messages.error(request, 'Unsuccessful Registration')

    form = RegistrationForm()
    return render(request, 'Account/signup.html', {'form':form})

def home(request):
    return render(request, 'home.html')
