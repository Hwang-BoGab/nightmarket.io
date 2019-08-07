from django.shortcuts import render

# Create your views here.
def temp(requests):
    return render(requests, 'temporary.html')
