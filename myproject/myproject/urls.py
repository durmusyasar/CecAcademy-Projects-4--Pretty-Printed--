from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include('hello.urls')),
    path('guestbook/', include('guestbook.urls')),
    path('', include('todo.urls')),
]
