# apps/bookmodule/urls.py

from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.index, name="index"),
    path('list_books/', views.list_books, name="list_books"),
path('<int:bookId>/', views.view_one_book, name="view_one_book"),
path('aboutus/', views.aboutus, name="aboutus"),

    # HTML5 pages
    path('html5/links/', views.html5_links, name="html5_links"),
    path('html5/text/formatting/', views.text_formatting, name="text_formatting"),
    path('html5/listing/', views.html5_listing, name="html5_listing"),
    path('html5/tables/', views.html5_tables, name="html5_tables"),
]