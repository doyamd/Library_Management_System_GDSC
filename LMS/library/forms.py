from django.forms import ModelForm
from .models import Book,Genre,Author,Publisher

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

class PublisherCreation(ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'