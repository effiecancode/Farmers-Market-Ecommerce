from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
# from django.contrib.auth.decorators import user_

from .forms import RegistrationForm


def activate_email(request, user, to_email):
    messages.success(request, f"Dear <b>{user}</b>, please go to your email <b>{to_email}</b> inbox and click on \
                     received activation link to confirm and complete the registration. <b>Note:</b> Check your dpam folder")

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active=False
            user.save()
            activate_email(request, user, form.cleaned_data.get("email"))
            # messages.success(request, 'Account Created Successfully', extra_tags="success")
            return redirect('Account:signin')
        else:
            messages.error(request, 'Unsuccessful Registration', extra_tags="error")

    form = RegistrationForm()
    return render(request, 'Account/signup.html', {'form':form})

