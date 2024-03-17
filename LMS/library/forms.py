from django.forms import ModelForm
from .models import Book,Genre,Author,Publisher,Review

class BookCreation(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class GenreCreation(ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'

class AuthorCreation(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class Reviewer(ModelForm):
    class Meta:
        model = Review
        fields = ['user', 'book', 'review']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        book = kwargs.pop('book', None)
        super(Reviewer, self).__init__(*args, **kwargs)

        if user and book:
            self.fields['user'].initial = user
            self.fields['book'].initial = book
            self.fields['user'].disabled = True
            self.fields['book'].disabled = True

class PublisherCreation(ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'
        
class BookUpdate(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'