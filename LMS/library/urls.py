from django.urls import path
from . import views

urlpatterns = [
    path('' , views.books_display , name = 'display-link'),
    path('loan/<int:book_id>/' , views.loan_book , name = 'loan-link'),
    path('loan_book_clicked/<int:book_id>/' , views.loan_book_clicked , name = 'loan-book-link'),
    path('loaned_books/<int:book_id>/' , views.loaned_books , name = 'loaned-book-link'),
] 