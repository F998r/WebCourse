from django.urls import path
from . import views   # Ensure this line is present and correct

urlpatterns = [
    path('',views.index, name='index'),
    path('books_list/',views.list_books, name='list_books'),
    path('<int:bookId>/',views.viewbook, name='view_book'),
    path('aboutus/',views.aboutus, name='aboutus'),
    # Add other URL patterns here
]
