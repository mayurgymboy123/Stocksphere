from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm, UserLoginForm, EditProfileForm

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect("users:login")
    else:
        form = UserRegistrationForm()
    return render(
        request,
        "users/register.html",
        {"form":form},
    )

def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect("users:profile")
            else:
                messages.error(
                    request,
                    "invalid username or password"
                )
                return redirect("users:login")
    else:
        form = UserLoginForm()
    return render(
        request,
        "users/login.html",
        {"form": form}
    )

def logout_view(request):
    logout(request)
    return redirect("users:login")

@login_required
def profile(request):
    return render(
        request,
        "users/profile.html"
    )

@login_required
def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("users:profile")
    else:
        form = EditProfileForm(instance=request.user)
    return render(
        request,
        "users/edit_profile.html",
        {"form": form}
    )