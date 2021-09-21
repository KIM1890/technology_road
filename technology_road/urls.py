from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('stores.urls')),
    path('todolist/', include('todo.urls')),
    path('admin/', admin.site.urls),
]
