from django.shortcuts import render

# Create your views here.

def logIn(request):
    return render(request , 'fronts/login.html')

def register(request):
    return render(request , 'fronts/register.html')

def home(request):
    return render(request , 'fronts/home.html')