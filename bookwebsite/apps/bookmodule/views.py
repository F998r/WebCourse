from django.shortcuts import render,get_object_or_404


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