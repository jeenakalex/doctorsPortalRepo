from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def home(request):
    return HttpResponse("Hello, Django!")

def hello_there(request, name):
    return render(
        request,
        'Hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )