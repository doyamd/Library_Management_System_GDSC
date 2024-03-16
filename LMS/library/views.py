from django.shortcuts import render, get_object_or_404, redirect
from django.http import request
from .models import Loan, Book
from django.contrib import messages
from datetime import datetime  
from .forms import BookForm


def books_display(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request , 'logged/display.html' , context)


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('logged/display.html')
    else:
        form = BookForm()
    return render(request, 'logged/addBook.html', {'form': form})

def loan_book_clicked(request, book_id):
    book = get_object_or_404(Book , id = book_id)
    context = {'book' : book}
    return render(request , 'logged/loan.html' , context)

def loan_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        username = request.POST.get('username')
        status = request.POST.get('status')
        user = User.objects.get(username=username)
        current_date = datetime.now() 
        loan = Loan.objects.create(book=book, user=user, check_out_date=current_date, status=status)
        loan.save()
        messages.success(request, 'Book successfully loaned.')
        return redirect('logged/display.html')  
    else:
        context = {'book': book}
        return render(request, 'logged/loan.html', context)


def loaned_books(request):
    loaned_books = Loan.objects.all()  
    return render(request, 'loaned_books.html', {'loaned_books': loaned_books})

