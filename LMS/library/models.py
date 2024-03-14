from django.db import models
from users.models import MyUser
from datetime import datetime,timedelta

# Create your models here.

class Author(models.Model):
    Author_name = models.CharField(max_length = 50)

class Publisher(models.Model):
    Publisher_name = models.CharField(max_length = 50)
    #contact info here
    #i believe its not needed :) 

class Genre(models.Model):
    Genre_name = models.CharField(max_length = 100)

class Book(models.Model):
    Title = models.CharField(max_length = 100)
    Publication_year = models.DateField()
    Number_of_copies = models.PositiveIntegerField()
    author = models.ForeignKey(Author , on_delete = models.SET_NULL , null = True)
    genre = models.ManyToManyField(Genre)
    publisher = models.ForeignKey(Publisher , on_delete = models.SET_NULL , null = True)
    cover = models.ImageField()#add width and height if needed


def expiry():
    return datetime.today() + timedelta(days=15)
class Loan(models.Model):
    book = models.ForeignKey(Book , on_delete = models.CASCADE)
    user = models.ForeignKey(MyUser , on_delete = models.CASCADE)
    check_out_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(default = expiry)
    status = models.CharField(max_length = 10)


class Fine(models.Model):
    loan = models.OneToOneField(Loan , on_delete = models.CASCADE)
    amount = models.IntegerField(max_length = 4)

    STATUS_CHOICES = [
        ('Completed', 'Completed'),
        ('Pending', 'Pending'),
    ]

    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    
class Likes(models.Model):
    user = models.ForeignKey(MyUser , on_delete = models.CASCADE)
    book = models.ForeignKey(Book , on_delete = models.CASCADE)

class Review(models.Model):
    user = models.ForeignKey(MyUser , on_delete = models.CASCADE)
    book = models.ForeignKey(Book , on_delete = models.CASCADE)
    review = models.TextField()



    







