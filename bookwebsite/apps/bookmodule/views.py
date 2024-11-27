from django.shortcuts import render,get_object_or_404 , redirect
from .models import Books,Address , Student,Student2,Products
from django.db.models import Q , Sum ,Count , Min , Max , Avg
from .forms import BookForm,studentForm, studentForm2,ProductsForm


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


def listbooks(request):
    obj = Books.objects.all()
    return render(request , "bookmodule/lab9_part1/listbooks.html" , {'obj' : obj})

def addbook(request):
    if request.method == "POST":
        title=request.POST.get('title')
        author=request.POST.get('author')
        price=request.POST.get('price')
        edition=request.POST.get('edition')

        obj = Books(title = title , author = author , price = price, edition = edition)
        obj.save()
        return redirect('listbooks')
    return render(request , "bookmodule/lab9_part1/addbook.html")



def updatebook(request , bID):
    obj=Books.objects.get(id = bID)
    if request.method == "POST":
        title=request.POST.get('title')
        author=request.POST.get('author')
        price=request.POST.get('price')
        edition=request.POST.get('edition')

        obj.title = title
        obj.author = author
        obj.price = price
        obj.edition = edition
        obj.save()

        return redirect('listbooks')

    return render(request , "bookmodule/lab9_part1/updatebook.html",{'obj':obj})


def deletebook(request , bID):
    obj = Books.objects.get(id = bID)
    if request.method == "POST":
        obj.delete()
        return redirect('listbooks')
    return render(request , "bookmodule/lab9_part1/deletebook.html",{'obj':obj})



def listbooks2(request):
    obj = Books.objects.all()
    return render(request , "bookmodule/lab9_part2/listbooks2.html" , {'obj' : obj})

def addbook2(request):   
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listbooks2')
        else:
            form = BookForm(None)
    return render(request , "bookmodule/lab9_part2/addbook2.html",{'form' : form})



def updatebbook2(request , bID):
    obj = Books.objects.get(id = bID)
    form = BookForm(instance = obj)
    if request.method == 'POST':
        form = BookForm(request.POST,instance = obj)
        if form.is_valid():
            form.save()
            return redirect('listbooks2')
        else:
            form=BookForm(instance=obj)
    return render(request , "bookmodule/lab9_part2/updatebook2.html",{'form':form})


def deletebook2(request , bID):
    obj = Books.objects.get(id = bID)
    form = BookForm(instance = obj)
    if request.method == 'POST':
        obj.delete()
        return redirect('listbooks2')

    return render(request , "bookmodule/lab9_part2/deletebook2.html",{'obj':obj})



def addStudent(request):
    form = studentForm()
    if request.method == "POST":
        form = studentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listStudent')
        else:
            form=studentForm(None)
    return render(request,"bookmodule/lab10/addStudent.html",{'form' : form})


def updateStudent(request,sID):
    obj = Student.objects.get(id = sID)
    form = studentForm(instance = obj)
    if request.method == "POST":
        form = studentForm(request.POST , instance = obj)
        if form.is_valid():
            form.save()
            return redirect('listStudent')
        else:
            form=studentForm(instance = obj)

    return render(request,"bookmodule/lab10/updateStudent.html",{'form' : form})


def delStudent(request,sID):
    obj = Student.objects.get(id = sID)
    form = studentForm(instance = obj) #to display the info of student
    if request.method == "POST":
        obj.delete()
        return redirect('listStudent')
    return render(request,"bookmodule/lab10/delStudent.html",{'form' : form})


def listStudent(request):
    obj = Student.objects.all()
    return render(request,"bookmodule/lab10/listStudent.html",{'obj' : obj})




    #------here is functions of many to many address for students


def addStudent2(request):
    form = studentForm2()
    if request.method == "POST":
        form = studentForm2(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listStudent2')
        else:
            form=studentForm2(None)
    return render(request,"bookmodule/lab10/addStudent2.html",{'form' : form})


def updateStudent2(request,sID):
    obj = Student2.objects.get(id = sID)
    form = studentForm2(instance = obj)
    if request.method == "POST":
        form = studentForm2(request.POST , instance = obj)
        if form.is_valid():
            form.save()
            return redirect('listStudent2')
        else:
            form=studentForm2(instance = obj)

    return render(request,"bookmodule/lab10/updateStudent2.html",{'form' : form})


def delStudent2(request,sID):
    obj = Student2.objects.get(id = sID)
    form = studentForm2(instance = obj) #to display the info of student
    if request.method == "POST":
        obj.delete()
        return redirect('listStudent2')
    return render(request,"bookmodule/lab10/deleteStudent2.html",{'form' : form})


def listStudent2(request):
    obj = Student2.objects.all()
    return render(request,"bookmodule/lab10/listStudent2.html",{'obj' : obj})

def prod(request):
    form = ProductsForm()
    if request.method == 'POST':
        form = ProductsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('prodList')
        else:
            form = ProductsForm(None)
    return render(request , 'bookmodule/lab10/prod.html',{'form' : form})

    

def prodList(request):
    products = Products.objects.all()
    return render(request,"bookmodule/lab10/prodList.html",{'products' : products})