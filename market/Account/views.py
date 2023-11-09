from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import RegistrationForm


def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active=False
            user.save()
            messages.success(request, 'Account Created Successfully', extra_tags="success")
            return redirect('Account:signin')
        else:
            messages.error(request, 'Unsuccessful Registration', extra_tags="error")

    form = RegistrationForm()
    return render(request, 'Account/signup.html', {'form':form})

