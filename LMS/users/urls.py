from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home , name = 'home-link'),
    path('register/' , views.register , name = 'register-link'),
    path('login/' , views.loginUser , name = 'login-link'),
    path('logout/'  ,views.logout_view, name = 'logout-link'),
]