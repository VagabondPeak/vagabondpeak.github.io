from django.http import HttpResponse

from django.shortcuts import render

def home(request):
    context = {
        'message': 'Hello, this is a dynamic message!',
    }
    return render(request, 'Homepage.html', context)

def homepage(request):
    return HttpResponse()

def login_view(request):
    return render(request, 'Loginpage.html')

def createAccount_view(request):
    return render(request, 'CreateAccount.html')

def aboutUs_view(request):
    return render(request, 'aboutUs.html')