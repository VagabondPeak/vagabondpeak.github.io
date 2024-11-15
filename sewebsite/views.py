from django.http import HttpResponse

from django.shortcuts import render

def home(request):
    context = {
        'message': 'Hello, this is a dynamic message!',
    }
    return render(request, 'Homepage.html', context)

def homepage(request):
    return HttpResponse()