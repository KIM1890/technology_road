from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.views import serve
from django.urls import path, include

urlpatterns = [
    path('', include('stores.urls')),
    path('admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
