from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PersonCreationForm
from .models import Person, City

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

def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_add')
    return render(request, 'form_.html', {'form': form})


def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'form_.html', {'form': form})


# AJAX
def load_cities(request):
    country_id = request.GET.get('country_id')
    cities = City.objects.filter(country_id=country_id).all()
    return render(request, 'city_dropdown_list_options.html', {'cities': cities})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)