from django.shortcuts import render
from .models import *

# Create your views here.
def home(requests):
    return render(requests, 'nolineApp/index.html')

def store(requests):
    return render(requests, 'nolineApp/store.html')

def category(requests):
    return render(requests, 'nolineApp/Category.html')

def review(requests):
    return render(requests, 'nolineApp/Review.html')

def contact(requests):
    return render(requests, 'nolineApp/Contact.html')


