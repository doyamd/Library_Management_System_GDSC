from django.shortcuts import render,get_object_or_404
from django.http import request
from .models import Book
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import BookCreation,GenreCreation,AuthorCreation,PublisherCreation

# Create your views here.

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
def loan_book(request, book_id):
    book = get_object_or_404(Book , id = book_id)
    context = {'book' : book}
    return render(request , 'logged/loan.html' , context)

@login_required
def search_book(request):
    searchItem = request.POST.get('search' , '')
    books = Book.objects.filter( Q(Title = searchItem) | Q(author__Author_name = searchItem) | Q(genre__Genre_name = searchItem) )

    context = {'books':set(books)}
    return render(request , 'logged/search.html' , context)

@login_required
def add_book(request):
    if request.method == 'POST':

        bookform = BookCreation(request.POST or None, prefix='book')
        genreform = GenreCreation(request.POST or None, prefix='genre')
        authorform = AuthorCreation(request.POST or None, prefix='author')
        publisherform = PublisherCreation(request.POST or None, prefix='publisher')

        if 'add_book' in request.POST and bookform.is_valid():
            book = bookform.save()

        elif 'add_genre' in request.POST and genreform.is_valid():
            genre = genreform.save()

        elif 'add_author' in request.POST and authorform.is_valid():
            author = authorform.save()

        elif 'add_publisher' in request.POST and publisherform.is_valid():
            publisher = publisherform.save()
    else:
        bookform = BookCreation(prefix='book')
        genreform = GenreCreation(prefix='genre')
        authorform = AuthorCreation(prefix='author')
        publisherform = PublisherCreation(prefix='publisher')

    context = {'bookform' : bookform ,
                'authorform' : authorform,
                'genreform' : genreform,
                'publisherform' : publisherform,
               }

    return render(request , 'logged/addBook.html' , context)
