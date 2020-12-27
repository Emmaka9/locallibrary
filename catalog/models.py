from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.

class Genre(models.Model):
    """ Model representing a book genre."""
    name = models.CharField(max_length=200, unique=True,help_text='Enter a book genre (e.g. Science Fiction)')

    def __str__(self):
        return self.name



class Author(models.Model):
    """Model representing an author."""
    # Fields
    first_name = models.CharField(max_length=100, help_text='First Name of the author')
    last_name = models.CharField(max_length=100, help_text='Last Name of the author.')
    date_of_birth = models.DateField(verbose_name='Born', null=True, blank=True, help_text='Year' 
    + ' the author was born')
    date_of_death = models.DateField(verbose_name='Died', null=True, blank=True, help_text='Year' 
    + ' the author died.')

    # metadata
    class Meta:
        ordering = ['last_name', 'first_name']
    
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.first_name} {self.last_name}'

    # reverse() == generateUrlFromViewName()
    
    def get_absolute_url(self):
        # returns a url that can be used to access a detail record for this model
        # for this to work we'll have to define a url mapping that has the name author-detail
        return reverse(viewname="author-detail", args=[str(self.id)])
    

class Language(models.Model):
    """Model representing the language of a book."""

    # Fields
    language = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.language





# Book model
class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)
    author = models.ForeignKey(to=Author, on_delete=models.SET_NULL, null=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in file.
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    isbn = models.CharField('ISBN', max_length=13,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn'
                                      '">ISBN number</a>')
    genre = models.ManyToManyField(to=Genre, help_text="Select a genre for this book")
    # ManyToManyField used because a genre can contain many books and a Book can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    language = models.ForeignKey(to=Language, on_delete=models.SET_NULL, null=True)

    def display_genre(self):
        """Creates a string for the Genre. This is required to display genre in Admin."""
        return ', '.join([genre.name for genre in self.genre.all()])

    display_genre.short_description = 'Genre'

    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('book-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    # class Meta:
    #     ordering = ['title']





import uuid # Required for unique book instances
from django.contrib.auth.models import User
from datetime import datetime

class BookInstance(models.Model):
    """Represents a specific copy of a book (i.e. that can be borrowed from the library)"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                           help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey(to=Book, on_delete=models.SET_NULL, null=True, related_name='copies')
    # a release/ version details
    imprint = models.CharField(max_length=200)
    borrowed = models.DateField(default=timezone.now().date(), verbose_name='borrowed date', null=True, blank=True)
    due_back = models.DateField(null=True, blank=True,)
    LOAN_STATUS = [
        ('m', 'Maintenance'),
        ('o', 'On Loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    ]
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability')
    borrower = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['due_back']
        permissions = (("can_mark_returned", "Set book as returned"),)

    def __str__(self):
        return f'id: {self.id}, title:{self.book.title}, status:{self.status}'

    @property
    def is_overdue(self):
        if self.due_back and datetime.today().date() > self.due_back:
            return True
        return False

    





