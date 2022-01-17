from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='shopHome'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('tracker', views.tracker, name='trackingStatus'),
    path('search', views.search, name='search'),
    path('productView', views.productView, name='productView'),
    path('checkout', views.checkout, name='checkout'),
]