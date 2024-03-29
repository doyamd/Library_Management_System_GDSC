from .forms import MyUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout



def loginUser(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_staff:
                    return redirect('display_staff-link')
                else:
                    return redirect('display-link')
            else:
                return redirect('register-link')
    else:
        form = AuthenticationForm()
    
    context = {'form': form}
    return render(request, 'fronts/login.html', context)

def register(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login-link')
    else:
        form = MyUserCreationForm()
    
    context = {'form' : form,}
    return render(request , 'fronts/register.html' , context)



def home(request):
    return render(request , 'fronts/home.html')

def logout_view(request):
    logout(request)
    return redirect('home-link')