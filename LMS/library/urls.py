from django.urls import path
from . import views

urlpatterns = [
    path('student/' , views.books_display , name = 'display-link'),
    path('staff/' , views.books_display_staff , name = 'display_staff-link'),
    path('loan/<int:book_id>/' , views.loan_book , name = 'loan-link'),
    path('search/', views.search_book , name = 'search-link'),
    path('addBook/' , views.add_book , name = 'addBook-link'),
] 