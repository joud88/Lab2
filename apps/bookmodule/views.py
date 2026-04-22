from django.shortcuts import render
from django.db.models import Q
from .models import Book
from django.db.models import Count, Sum, Avg, Max, Min
from .models import Book, Student ,Publisher





def lab9_task1(request):
    books = Book.objects.all()
    total_quantity = Book.objects.aggregate(total=Sum('quantity'))['total'] or 0

    for book in books:
        if total_quantity > 0:
            book.percentage_availability = round((book.quantity / total_quantity) * 100, 2)
        else:
            book.percentage_availability = 0

    return render(request, 'bookmodule/lab9_task1.html', {'books': books})


def lab9_task2(request):
    publishers = Publisher.objects.annotate(total_book_stock=Sum('book__quantity'))

    return render(request, 'bookmodule/lab9_task2.html', {'publishers': publishers})



def lab9_task3(request):
    publishers = Publisher.objects.annotate(oldest_book_date=Min('book__pubdate'))

    return render(request, 'bookmodule/lab9_task3.html', {'publishers': publishers})


def lab9_task4(request):
    publishers = Publisher.objects.annotate(
        avg_price=Avg('book__price'),
        min_price=Min('book__price'),
        max_price=Max('book__price')
    )
    return render(request, 'bookmodule/lab9_task4.html', {'publishers': publishers})



def lab9_task5(request):
    publishers = Publisher.objects.annotate(
        high_rated_books_count=Count('book', filter=Q(book__rating__gte=4))
    )

    return render(request, 'bookmodule/lab9_task5.html', {'publishers': publishers})



def lab9_task6(request):
    publishers = Publisher.objects.annotate(
        filtered_books_count=Count(
            'book',
            filter=Q(book__price__gt=50, book__quantity__lt=5, book__quantity__gte=1)
        )
    )

    return render(request, 'bookmodule/lab9_task6.html', {'publishers': publishers})




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