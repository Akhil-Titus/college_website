from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password0 = request.POST['password0']
        user  = auth.authenticate(username=username,
                                  password=password0)
        if user is not None:
            auth.login(request, user)
            return redirect('/credentials_app/profile')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    return render(request, "login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password0 = request.POST['password0']
        password1 = request.POST['password1']

        if password0==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('/credentials_app/register') #
            else:
                user = User.objects.create_user(username=username,
                                                password=password0)
                user.save();
                #print('User Created')
                return redirect('/credentials_app/login')
        else:
            messages.info(request, "password not matching")
            return redirect('/credentials_app/register') #
        return redirect('/')
    return render(request, "register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def profile(request):
    return render(request, 'profile.html')

from .models import Department, Course
from .forms import FormAppForm

def form_view(request):
    if request.method == 'POST':
        form = FormAppForm(request.POST)
        if form.is_valid():
            # Process form data and display the success message
            return render(request, 'success.html')
    else:
        form = FormAppForm()

    return render(request, 'form_.html', {'form': form})