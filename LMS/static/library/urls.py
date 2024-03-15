from django.urls import path
from . import views

urlpatterns = [
    path('' , views.books_display , name = 'display-link'),
    path('loan/<int:book_id>/' , views.loan_book , name = 'loan-link'),
] 