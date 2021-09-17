from django.urls import path
from . import views

urlpatterns = [
    path('', views.StorePageView.as_view(), name="store"),
    path('ipad/', views.IpadPageView.as_view(), name="ipad"),
    path('iphone/', views.IphonePageView.as_view(), name="iphone"),
    path('watch/', views.IpadPageView.as_view(), name="watch"),
    path('tv/', views.IpadPageView.as_view(), name="tv"),
    path('support/', views.IpadPageView.as_view(), name="support"),
    path('cart/', views.IpadPageView.as_view(), name="cart"),
]
