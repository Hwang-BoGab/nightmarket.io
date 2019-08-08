from django.shortcuts import render

# Create your views here.
def store(requests):
    return render(requests, 'store_index.html')