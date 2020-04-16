from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User


def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['first_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username alrady taken .")
                return redirect(register)
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email alrady taken .")
                return redirect(register)
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password, first_name=first_name, last_name=last_name)
                user.save()
                messages.success(request, "You are registred. Sign in")
                return redirect('login')
        else:
            messages.error(request, "Passwords do not match")
        return render(request, "accounts/register.html")
    else:
        return render(request, "accounts/register.html")


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are in")
            return redirect('dashboard')
        else:
            messages.error(request, "Login or password incorrect")
            return redirect('login')
    else:
        return render(request, "accounts/login.html")


def logout(request):
    if request.method == "POST":
        auth.logout(request)
    messages.success(request, "See you later.")
    return redirect('index')


def dashboard(request):
    return render(request, "accounts/dashboard.html")


def dashboard_setings(request):
    return render(request, "accounts/dashboard_setings.html")
