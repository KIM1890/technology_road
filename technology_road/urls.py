from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.views import serve
from django.urls import path, include

urlpatterns = [
    path('', include('stores.urls')),
    path('admin/', admin.site.urls),
]
