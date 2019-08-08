from django.contrib import admin
from django.urls import path, include
from nolineApp import views
import accounts.views
import temporary.views
import stores.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('category/', views.category, name='ca
    h('review/', views.review, name='review'),
    path('contact/',  views.contact, name='contact'),
    path('accounts/',include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('temp/', temporary.views.temp, name="temp"),
    path('store/', stores.views.store, name="store"),
]
