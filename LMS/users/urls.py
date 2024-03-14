from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home , name = 'home-link'),
    path('login/' ,views.logIn , name = 'login-link'),
    path('register/' , views.register , name = 'register-link')
]