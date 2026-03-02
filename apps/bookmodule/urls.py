print(">>> BOOKMODULE URLS LOADED <<<")

from django.urls import path
from . import views

app_name = "books"   # ✅ REQUIRED for {% url 'books.index' %}

urlpatterns = [
    path('', views.index, name="index"),
    path('list_books/', views.list_books, name="list_books"),
    path('<int:bookId>/', views.viewbook, name="view_one_book"),
    path('aboutus/', views.aboutus, name="aboutus"),
]