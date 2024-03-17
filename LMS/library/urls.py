from django.urls import path
from . import views

urlpatterns = [
    path('student/' , views.books_display , name = 'display-link'),
    path('staff/' , views.books_display_staff , name = 'display_staff-link'),
    path('loan/<int:book_id>/' , views.loan_book , name = 'loan-link'),
    path('search/', views.search_book , name = 'search-link'),
    path('addBook/' , views.add_book , name = 'addBook-link'),
    path('addGenre/' , views.add_genre , name = 'addGenre-link'),
    path('addAuthor/' , views.add_author , name = 'addAuthor-link'),
    path('addPublisher/' , views.add_pulisher , name = 'addPublisher-link'),
    path('loan_book_clicked/<int:book_id>/' , views.loan_book_clicked , name = 'loan-book-link'),
    path('loan/<int:book_id>/<int:user_id>/' , views.loan_book , name = 'loan-link'),
    path('loaned_books/' , views.loaned_books , name = 'loaned-book-link'),
    path('return_book_request/<int:loan_id>/' , views.grant_request , name = 'return_req-link'),
    path('return_request/<int:loan_id>/' , views.request_return , name = 'req-link'),
    path('return_request_page/' , views.display_req , name = 'req_page-link'),
    path('like/<int:loan_id>/' , views.like , name = 'like-link'),
    path('like_page/<int:loan_id>/' , views.like_page , name = 'like_page-link'),
    path('update_book/<int:book_id>/', views.update_book, name='update-link'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete-link'),
    path('delete_book_page/<int:book_id>/', views.delete_page, name='delete_page-link'),
    path('bookDetails/<int:book_id>/' , views.bookDetail , name = 'bookDetail-link'),
] 