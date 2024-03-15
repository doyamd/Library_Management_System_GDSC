from django.shortcuts import render
from .forms import MyUserCreationForm
# Create your views here.

def logIn(request):
    return render(request , 'fronts/login.html')

def register(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MyUserCreationForm()
    
    context = {'form' : form,
               }
    return render(request , 'fronts/register.html' , context)

def home(request):
    return render(request , 'fronts/home.html')