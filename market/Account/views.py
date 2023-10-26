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
            messages.success(request, 'Account Created Successfully')
            return redirect('Account:home')
        else:
            messages.error(request, 'Unsuccessful Registration')

    form = RegistrationForm()
    return render(request, 'Account/signup.html', {'form':form})

def home(request):
    return render(request, 'home.html')

@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user

            profile.save()

            messages.success(request, "Profile created successfully!")
            return redirect("dashboard:index")
        else:
            messages.error(request, "Unsuccessfull!!")


    form = ProfileForm()

    return render(request, "Account/profile.html", {"form":form})


@login_required
def update_profile(request, id):

    profile = get_object_or_404(Profile, id=id, user=request.user)

    if request.method == "POST":
        form = UpdateProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()

            return redirect("Account:profile", id=profile.id)
    else:
        form = UpdateProfileForm(instance=profile)

    context = {
        "form": form
    }

    return render(request, "product/update_product.html", context)

@login_required
def delete_profile(request, id):
    product = get_object_or_404(Profile, id=id, user=request.user)
    product.delete()

    return redirect('product:home')