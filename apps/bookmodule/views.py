from django.shortcuts import render
from django.db.models import Q
from .models import Book
from django.db.models import Count, Sum, Avg, Max, Min
from .models import Book, Student




def lab8_task1(request):
    books = Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/lab8_task1.html', {'books': books})


def lab8_task2(request):
    books = Book.objects.filter(
        Q(edition__gt=3) & (Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/lab8_task2.html', {'books': books})

def lab8_task3(request):
    books = Book.objects.filter(
        Q(edition__lte=3) & ~(Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/lab8_task3.html', {'books': books})

def lab8_task4(request):
    books = Book.objects.order_by('title')
    return render(request, 'bookmodule/lab8_task4.html', {'books': books})

def lab8_task5(request):
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        average_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/lab8_task5.html', {'stats': stats})

def lab8_task7(request):
    students_per_city = Student.objects.values('address__city').annotate(
        student_count=Count('id')
    ).order_by('address__city')

    return render(request, 'bookmodule/lab8_task7.html', {
        'students_per_city': students_per_city
    })


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