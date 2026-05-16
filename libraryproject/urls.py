# libraryproject/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from apps.bookmodule import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('apps.bookmodule.urls')),
    path('users/register/', views.register_user, name='register'),
    path('users/login/', views.login_user, name='login'),
    path('users/logout/', views.logout_user, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)