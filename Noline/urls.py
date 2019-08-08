from django.contrib import admin
from django.urls import path, include
from nolineApp import views
from django.shortcuts import render, get_object_or_404, redirect
import accounts.views
import temporary.views
import stores.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('review/', views.review, name='review'),
    path('category/', views.category, name='category'),
    path('contact/',  views.contact, name='contact'),
    path('accounts/',include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('temp/', temporary.views.temp, name="temp"),
    #/(?P<blog_id>[0-9]+)/
    path('store/<int:pk>/', stores.views.store, name="store"),
    
]
