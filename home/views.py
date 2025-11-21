from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout

def home_view(request):
    return render(request, "home/index.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/dashboard/")   # SUCCESS → go to dashboard
        else:
            messages.error(request, "Invalid username or password")  # ERROR

    return render(request, "home/login.html")


def logout_view(request):
    logout(request)
    return redirect("/login/")





def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        login(request, user)
        return redirect("/")

    return render(request, "home/register.html")

@login_required
def dashboard_view(request):
    return render(request, "home/dashboard.html")


