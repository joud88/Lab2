# libraryproject/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include(('apps.bookmodule.urls', 'books'), namespace='books')),
    # Add other apps here if needed
]