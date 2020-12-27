from django.urls import path
from . import views

'''
 URL mappings are managed though the urlpatterns variable - a python list of path() funcions.
 Each path() function either associates a URL pattern to a specific view, (which will be displayed when a pattern is matched)
 or another list of URL pattern testing code (in this second case the pattern becomes "base url"
 for patterns defined in the target module). 
'''

'''
The route in path() is a string - defining a 'url pattern' to match 
'''
urlpatterns = [
    path(route='',view=views.index, name='index'),
    path(route='books/', view=views.BookListView.as_view(), name='books'),
    # here angle bracket define the part of the url to be captured,
    # enclosing the name of the variable that the view can use to access the captured data
    path(route='book/<int:pk>', view=views.BookDetailView.as_view(), name='book-detail'),
    path(route='author/', view=views.AuthorListView.as_view(), name='authors'),
    path(route='author/<int:pk>', view=views.AuthorDetailView.as_view(), name= 'author-detail'),
    path(route='mybooks/', view=views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path(route=r'borrowed/', view=views.LoanedBooksByAllListView.as_view(), name='all-borrowed'),
    #path(r'borrowed/<int:bookinst_id>', views.LoanedBooksDetailView.as_view(), name='renew-book-librarian'),
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),

]



