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
