from django.shortcuts import render, get_object_or_404, redirect
from django.http import request
from .models import Loan, Book, ReturnRequest,Fine , Likes , Review
from users.models import MyUser
from django.contrib import messages
from datetime import datetime  
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import BookCreation,GenreCreation,AuthorCreation,PublisherCreation,Reviewer, BookUpdate



@login_required
def books_display(request):
    loans = Loan.objects.all()
    books = set(Book.objects.all())
    context = {'books': books , 'loans' : loans}
    return render(request , 'logged/display.html' , context)

@login_required
def books_display_staff(request):
    books = set(Book.objects.all())
    context = {'books': books}
    return render(request , 'logged/staff.html' , context)

@login_required
def loan_book_clicked(request, book_id):
    book = get_object_or_404(Book , id = book_id)
    context = {'book' : book}
    return render(request , 'logged/loan.html' , context)

@login_required
def loan_book(request, book_id , user_id):
    book = get_object_or_404(Book, id=book_id)
    user_loans = Loan.objects.filter(user__id=user_id).count()
    book_loans = Loan.objects.filter(book__id = user_id).count()

    context = {'book': book}

    if user_loans < 6 and book_loans < book.Number_of_copies:
        if request.method == 'POST':
            user = get_object_or_404(MyUser , id=user_id)
            current_date = datetime.now() 
            loan = Loan.objects.create(book=book, user=user, check_out_date=current_date )
            loan.save()
            messages.success(request, f'{book.Title} successfully loaned.')
            return redirect('display-link')
        
        else:
            messages.info(request, 'The book is not available for loan.')
            context = {'book': book}
            return render(request, 'logged/loan.html', context)

    else:
        messages.error(request, 'You have reached your loan limit or there are no copies left.')
        return render(request, 'logged/loan.html', context)

@login_required
def loaned_books(request ):
    loaned_books = Loan.objects.all()  
    return render(request, 'logged/loanedBooks.html', {'loaned_books': loaned_books})



@login_required
def search_book(request):
    searchItem = request.POST.get('search' , '')
    books = Book.objects.filter( Q(Title = searchItem) | Q(author__Author_name = searchItem) | Q(genre__Genre_name = searchItem) )

    context = {'books':set(books)}
    return render(request , 'logged/search.html' , context)


@login_required
def add_book(request):
    if request.method == 'POST':
        bookform = BookCreation(request.POST , request.FILES)

        if bookform.is_valid():
            bookform.save()
            return redirect('display_staff-link')

    else:
        bookform = BookCreation()

    context = {'bookform' : bookform ,
      
               }

    return render(request , 'logged/addBook.html' , context)


@login_required
def add_genre(request):
    if request.method == 'POST':
        genreform = GenreCreation(request.POST)

        if genreform.is_valid():
           genreform.save()
           return redirect('display_staff-link')

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
        
        if authorform.is_valid():
            authorform.save()
            return redirect('display_staff-link')

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

        if publisherform.is_valid():
            publisherform.save()
            return redirect('display_staff-link')
    else:
        publisherform = PublisherCreation()

    context = {
                'publisherform' : publisherform,
               }

    return render(request , 'logged/addPublisher.html' , context)


@login_required
def grant_request(request , loan_id):
    loan = Loan.objects.get( id=loan_id )
    messages.success(request, f'{loan.book.Title} successfully returned.')
    loan.delete()
    return redirect('display_staff-link')

@login_required
def request_return(request , loan_id):
    loan_obj = Loan.objects.get(id = loan_id)

    fine_amount = 0.0
    if loan_obj.return_date.day - loan_obj.check_out_date.day > 15:
        overdue = 15 - (loan_obj.return_date.day - loan_obj.check_out_date.day)
        fine_amount = overdue * 10.0

    fine_obj = Fine(loan = loan_obj , amount = fine_amount)
    fine_obj.save()
    request_obj =  ReturnRequest(loan = loan_obj , fine = fine_obj)
    
    if request.method == 'POST':
        form = Reviewer(request.POST , user = loan_obj.user , book = loan_obj.book)
        if form.is_valid():
            form.save()
            request_obj.save()
            messages.success(request, f'Request to return {loan_obj.book.Title} successfull.')
            return redirect('like_page-link' , loan_id )
    else:
        form = Reviewer(user = loan_obj.user , book = loan_obj.book)
        

    context = {'loan':loan_obj , 'form':form}
    return render(request , 'logged/review.html' , context)


@login_required
def display_req(request):
    reqs = ReturnRequest.objects.all()
    context = {'reqs': reqs}
    return render(request , 'logged/returnReq.html' , context)

@login_required
def like(request , loan_id):
    loan_obj = Loan.objects.get(id = loan_id)
    book_obj = loan_obj.book
    user_obj = loan_obj.user
    like_obj = Likes(user = user_obj , book = book_obj)
    like_obj.save()
    return redirect('display-link')

@login_required
def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookUpdate(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('display_staff-link')  
    else:
        form = BookUpdate(instance=book)
    
    return render(request, 'logged/updateBook.html', {'form': form, 'book': book})


@login_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    messages.success(request, f'{book.Title} successfully deleted.')
    book.delete()
    return redirect('display_staff-link')
  
    # messages.success(request, f'{book.Title} not deleted.')
    # return render(request, 'logged/deleteBook.html', {'book': book})

@login_required
def delete_page(request , book_id):
    book = get_object_or_404(Book, id=book_id)
    context = {'book': book}
    return render(request, 'logged/deleteBook.html', context)

@login_required
def like_page(request , loan_id):
    loan = get_object_or_404(Loan, id=loan_id)
    context = {'loan': loan}
    return render(request, 'logged/like.html', context)

@login_required
def bookDetail(request , book_id):
    book = Book.objects.get(id = book_id)
    likes = Likes.objects.filter(book__id = book_id).count()
    reviews = Review.objects.filter(book__id = book_id)

    context = {'book':book, 'likes':likes , 'reviews':reviews}

    return render(request , 'logged/bookDetail.html' , context)
