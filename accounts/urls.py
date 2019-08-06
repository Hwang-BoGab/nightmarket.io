from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.join, name='join'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]