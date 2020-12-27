from django.contrib import admin
from .models import *

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class BookInline(admin.TabularInline):
    model = Book
    extra = 0

class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'date_of_birth',
        'date_of_death',
    ]
    inlines = [BookInline,]

    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

# Register the admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'author',
        'summary',
        'display_genre',
        'isbn',
        'language',
    ]
    inlines = [BookInstanceInline]

    filter_horizontal=('genre',)



class BookInstanceAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'book',
        'imprint',
        'borrowed',
        'status',
        'borrower',
        'due_back',
    ]

    fieldsets = (
        (None, {
            "fields": (
                'book', 'imprint', 'id'
            ),
        }),
        ('Availability',{
            'fields': ('status', 'borrowed', 'due_back', 'borrower')
        })
    )
    


# Register your models here.# Register your models here.

admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Language)
#admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
