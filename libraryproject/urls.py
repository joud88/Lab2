from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # bookmodule
    path('books/', include(('apps.bookmodule.urls', 'books'), namespace='books')),

    # usermodule (KEEP IT, but namespaced)
    path('users/', include(('apps.usermodule.urls', 'users'), namespace='users')),
]