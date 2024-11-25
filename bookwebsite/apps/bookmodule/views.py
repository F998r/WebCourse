from django.shortcuts import render,get_object_or_404
from .models import Books,Address , Student
from django.db.models import Q , Sum ,Count , Min , Max , Avg


def index(request):
    context = { 
        'course' : 'web techonlogy'
        }
    return render(request, 'bookmodule/index.html')

def list_books(request):
    return render(request,'bookmodule/books_list.html')



def viewbook(request, bookId):
    # Map bookId to template names
    templates = {
        1: 'bookmodule/book_one.html',
        2: 'bookmodule/book_two.html',
        3: 'bookmodule/book_three.html'
    }

    # Get the template based on bookId
    template_name = templates.get(bookId)

    return render(request, template_name)


def aboutus(request):
    return render(request,'bookmodule/aboutus.html')

def qu(request):
    return render(request, "bookmodule/qassimUn.html")

def format(request):
    return render(request, "bookmodule/formatting.html")

def lists(request):
    return render(request,"bookmodule/listing.html")


def tables(request):
    return render(request,"bookmodule/table.html")

def __getBookList():
    book1 = { 'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J.Humble and D. Farly'}
    book2 = { 'id': 56788765, 'title': 'Reversing: Secrest of Reverse Engineering', 'author': 'E. Eilam' }
    book3 = { 'id': 43211234, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov'}
    return [book1 , book2 , book3]


def srch(request):
    if request.method == "POST":
        key = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        #do filter
        books= __getBookList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and key in item['title'].lower(): 
                contained = True
            if not contained and isAuthor and key in item['author'].lower():
                contained = True

            if contained:
                newBooks.append(item)
        return render(request, 'bookmodule/BookList.html', {'books' : newBooks})
 
    return render(request, "bookmodule/search.html")

def simple_query(request):
    if request.method == "POST":
        key = request.POST.get('keyW', '').lower()  # Fetch and convert to lowercase
        books = Books.objects.all()  # Retrieve all books from the database
        filtered_books = [] 

        for obj in books:
           filtered_books= Books.objects.filter(title__icontains = key)
        
        return render(request, 'bookmodule/BookList.html', {'books': filtered_books})

    return render(request, "bookmodule/Query.html")


def task1(request):
    obj = Books.objects.filter(Q(price__lte=50))
    return render(request , "bookmodule/lab8/task1.html",{'obj' : obj})

def task2(request):
    obj=Books.objects.filter(Q(edition__gt=2) & (Q(title__icontains='qu') | Q(author__icontains='qu')))
    return render(request , "bookmodule/lab8/task2.html", {'obj' : obj})

def task3(request):
    obj = Books.objects.filter(Q(edition__lte=2) & (~Q(title__icontains='qu') | ~Q(author__icontains='qu')))
    return render(request , "bookmodule/lab8/task3.html", {'obj' : obj})

def task4(request):
    obj = Books.objects.all().order_by('title')
    return render(request , "bookmodule/lab8/task4.html", {'obj' : obj})

def task5(request):
    obj=Books.objects.all()
    count = Books.objects.aggregate(Count('price'))
    total = Books.objects.aggregate(Sum('price'))
    average = Books.objects.aggregate(Avg('price'))
    maximum = Books.objects.aggregate(Max('price'))
    minimum = Books.objects.aggregate(Min('price'))
    context = {
        'count' : count,
        'total' : total,
        'average' : average,
        'maximum' : maximum,
        'minimum' : minimum
    }
    return render(request , "bookmodule/lab8/task5.html" , context)

def task6(request):
    addObj = Address.objects.all()
    cities = {} #dictionary
    for i in addObj:
        studentCount = Student.objects.filter(address = i).count()
        cities[i.city] = studentCount



    return render(request , "bookmodule/lab8/task6.html" , {'cities':cities})
 
