from django.shortcuts import render, get_object_or_404, redirect
from django.http import request
from .models import Loan, Book
from users.models import MyUser
from django.contrib import messages
from datetime import datetime  
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import BookCreation,GenreCreation,AuthorCreation,PublisherCreation


@login_required
def books_display(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request , 'logged/display.html' , context)

@login_required
def books_display_staff(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request , 'logged/staff.html' , context)

@login_required
def loan_book_clicked(request, book_id):
    book = get_object_or_404(Book , id = book_id)
    context = {'book' : book}
    return render(request , 'logged/loan.html' , context)

@login_required
def loan_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        username = request.POST.get('username')
        status = request.POST.get('status')
        user = MyUser.objects.get(username=username)
        current_date = datetime.now() 
        loan = Loan.objects.create(book=book, user=user, check_out_date=current_date, status=status)
        loan.save()
        messages.success(request, f'{book.Title} successfully loaned.')
        return redirect('display-link')
    
    else:
        context = {'book': book}
        return render(request, 'logged/loan.html', context)

@login_required
def loaned_books(request):
    loaned_books = Loan.objects.all()  
    return render(request, 'loaned_books.html', {'loaned_books': loaned_books})



@login_required
def search_book(request):
    searchItem = request.POST.get('search' , '')
    books = Book.objects.filter( Q(Title = searchItem) | Q(author__Author_name = searchItem) | Q(genre__Genre_name = searchItem) )

    context = {'books':set(books)}
    return render(request , 'logged/search.html' , context)


@login_required
def add_book(request):
    if request.method == 'POST':
        bookform = BookCreation(request.POST)


        if 'add_book' in request.POST and bookform.is_valid():
            book = bookform.save()

    else:
        bookform = BookCreation()

    context = {'bookform' : bookform ,
      
               }

    return render(request , 'logged/addBook.html' , context)


@login_required
def add_genre(request):
    if request.method == 'POST':
  
        genreform = GenreCreation(request.POST)


        if 'add_genre' in request.POST and genreform.is_valid():
            genre = genreform.save()

    else:
        genreform = GenreCreation()
    context = {
                'genreform' : genreform,
               }

    return render(request , 'logged/addGenre.html' , context)


@login_required
def add_author(request):
    if request.method == 'POST':
        authorform = AuthorCreation(request.POST )
        
        if 'add_author' in request.POST and authorform.is_valid():
            author = authorform.save()

    else:
        authorform = AuthorCreation()

    context = {
                'authorform' : authorform,
   
               }

    return render(request , 'logged/addAuthor.html' , context)


@login_required
def add_pulisher(request):
    if request.method == 'POST':
        publisherform = PublisherCreation(request.POST)

        if 'add_publisher' in request.POST and publisherform.is_valid():
            publisher = publisherform.save()
    else:
        publisherform = PublisherCreation()

    context = {
                'publisherform' : publisherform,
               }

    return render(request , 'logged/addPublisher.html' , context)
