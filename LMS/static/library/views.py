from django.shortcuts import render,get_object_or_404
from django.http import request
from .models import Book

# Create your views here.

def books_display(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request , 'logged/display.html' , context)

def loan_book(request, book_id):
    book = get_object_or_404(Book , id = book_id)
    context = {'book' : book}
    return render(request , 'logged/loan.html' , context)


