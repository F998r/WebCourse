from django.urls import path
from . import views   # Ensure this line is present and correct

urlpatterns = [
    path('', views.index, name='index'),
    path('books_list/', views.list_books, name='list_books'),
    path('<int:bookId>/', views.viewbook, name='view_book'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('links', views.qu, name="qassimUn"),
    path('formmating', views.format, name="formatting"),
    path('listing', views.lists, name="listing"),
    path('tables', views.tables, name="tables")
    # Add other URL patterns here
]
