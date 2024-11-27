from django.urls import path
from . import views   # Ensure this line is present and correct
from django.conf.urls.static import static
from django.conf import settings

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
    path('lab9_part1/listbooks' , views.listbooks, name="listbooks"),
    path('lab9_part1/addbook' , views.addbook, name="addbook"),
    path('lab9_part1/updatebook/<int:bID>' , views.updatebook, name="updatebook"),
    path('lab9_part1/deletebook/<int:bID>' , views.deletebook, name="deletebook"),

    path('lab9_part2/listbooks2' , views.listbooks2, name="listbooks2"),
    path('lab9_part2/addbook2' , views.addbook2, name="addbook2"),
    path('lab9_part2/updatebook2/<int:bID>' , views.updatebbook2, name="updatebook2"),
    path('lab9_part2/deletebook2/<int:bID>' , views.deletebook2, name="deletebook2"),


    path('lab10/addStudent' , views.addStudent, name="addStudent"),
    path('lab10/updateStudent/<int:sID>' , views.updateStudent, name="updateStudent"),
    path('lab10/deltudent/<int:sID>' , views.delStudent, name="delStudent"),
    path('lab10/listStudent' , views.listStudent, name="listStudent"),

    path('lab10/addStudent2' , views.addStudent2, name="addStudent2"),
    path('lab10/updateStudent2/<int:sID>' , views.updateStudent2, name="updateStudent2"),
    path('lab10/deltudent2/<int:sID>' , views.delStudent2, name="delStudent2"),
    path('lab10/listStudent2' , views.listStudent2, name="listStudent2"),
    path('lab10/products' , views.prod , name="products"),
    path('lab10/productsList' , views.prodList , name="prodList"),
    # Add other URL patterns here
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

