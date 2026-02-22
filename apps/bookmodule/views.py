# apps/bookmodule/views.py
from django.shortcuts import render

def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html", {"name": name})
def index2(request, val1=0):
    return render(request, "bookmodule/index2.html", {"val1": val1})

def viewbook(request, bookId):
    # Simulate some books (later you can fetch from DB)
    book1 = {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
    book2 = {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    
    targetBook = None
    if book1['id'] == bookId:
        targetBook = book1
    elif book2['id'] == bookId:
        targetBook = book2

    context = {'book': targetBook}  # Variable accessible by template
    return render(request, 'bookmodule/show.html', context)