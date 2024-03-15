from django.db import models
from users.models import MyUser
from datetime import datetime,timedelta

# Create your models here.

class Author(models.Model):
    Author_name = models.CharField(max_length = 50)
    def __str__(self):
        return self.Author_name

class Publisher(models.Model):
    Publisher_name = models.CharField(max_length = 50)
    #contact info here
    #i believe its not needed :) 
    def __str__(self):
        return self.Publisher_name

class Genre(models.Model):
    Genre_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.Genre_name


class Book(models.Model):
    Title = models.CharField(max_length = 100)
    Publication_year = models.DateField()
    Number_of_copies = models.PositiveIntegerField()
    author = models.ForeignKey(Author , on_delete = models.SET_NULL , null = True)
    genre = models.ManyToManyField(Genre)
    publisher = models.ForeignKey(Publisher , on_delete = models.SET_NULL , null = True)
    cover = models.ImageField(upload_to='covers/')#add width and height if needed
    
    @property
    def likes(self):
        return self.likes_set.count()
    class Meta:
        ordering = ['-likes']

    def __str__(self):
        return self.Title

def expiry():
    return datetime.today() + timedelta(days=15)
class Loan(models.Model):
    book = models.ForeignKey(Book , on_delete = models.CASCADE)
    user = models.ForeignKey(MyUser , on_delete = models.CASCADE)
    check_out_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(default = expiry)
    status = models.CharField(max_length = 10)

    def __str__(self):
        return f'by : {self.user.username} book: {self.book.Title}'


class Fine(models.Model):
    loan = models.OneToOneField(Loan , on_delete = models.CASCADE)
    amount = models.IntegerField()

    STATUS_CHOICES = [
        ('Completed', 'Completed'),
        ('Pending', 'Pending'),
    ]

    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    def __str__(self):
        return self.amount
    
class Likes(models.Model):
    user = models.ForeignKey(MyUser , on_delete = models.CASCADE)
    book = models.ForeignKey(Book , on_delete = models.CASCADE)

class Review(models.Model):
    user = models.ForeignKey(MyUser , on_delete = models.CASCADE)
    book = models.ForeignKey(Book , on_delete = models.CASCADE)
    review = models.TextField()
    def __str__(self):
        return f'by: {self.user.username}'



    







