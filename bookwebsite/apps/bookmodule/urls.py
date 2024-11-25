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
    path('tables', views.tables, name="tables"),
    path('search',views.srch,name="search"),
    path('simpleQuery' , views.simple_query , name = "simpleQ"),
    path('lab8/task1' , views.task1, name="task1"),
    path('lab8/task2' , views.task2, name="task2"),
    path('lab8/task3' , views.task3, name="task3"),
    path('lab8/task4' , views.task4, name="task4"),
    path('lab8/task5' , views.task5, name="task5"),
    path('lab8/task6' , views.task6, name="task6"),
    # Add other URL patterns here
]
