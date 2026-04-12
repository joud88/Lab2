from django.shortcuts import render
from .models import Book


def search_books(request):
    if request.method == "POST":
        string = request.POST.get('keyword', '').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        books = Book.objects.all()
        newBooks = []

        for item in books:
            contained = False

            if isTitle and string in item.title.lower():
                contained = True

            if not contained and isAuthor and string in item.author.lower():
                contained = True

            if contained:
                newBooks.append(item)

        return render(request, 'bookmodule/bookList.html', {'books': newBooks})

    return render(request, 'bookmodule/search.html')


def index(request):
    return render(request, "bookmodule/index.html")


def list_books(request):
    books = Book.objects.all()
    return render(request, "bookmodule/bookList.html", {'books': books})


def view_one_book(request, bookId):
    book = Book.objects.get(id=bookId)
    return render(request, "bookmodule/one_book.html", {'book': book})


def aboutus(request):
    return render(request, "bookmodule/aboutus.html")


def html5_links(request):
    return render(request, "bookmodule/html5_links.html")


def text_formatting(request):
    return render(request, "bookmodule/text_formatting.html")


def html5_listing(request):
    return render(request, "bookmodule/listing.html")


def html5_tables(request):
    return render(request, "bookmodule/tables.html")


def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})


def complex_query(request):
    mybooks = Book.objects.filter(
        author__isnull=False
    ).filter(
        title__icontains='and'
    ).filter(
        edition__gte=2
    ).exclude(
        price__lte=100
    )[:10]

    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')