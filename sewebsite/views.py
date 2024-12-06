from django.http import HttpResponse
from django.shortcuts import render, redirect
from accounts.forms import UserAccountForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from accounts.forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout


def home(request):
    context = {
        'message': 'Hello, this is a dynamic message!',
    }
    return render(request, 'Homepage.html', context)

def homepage(request):
    return HttpResponse()

def message_view(request):
    # Logic for displaying messages can go here
    return render(request, 'message.html')

def login_view(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('messages')
        
        context = {}
    return render(request, 'Loginpage.html')

def createAccount_view(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account created for ' + user)
            
            return redirect('login')
            
    context = {'form':form}
    return render(request, 'CreateAccount.html', context)

def aboutUs_view(request): 
    return render(request, 'aboutUs.html')

def create_account(request):
    if request.method == 'POST':
        form = UserAccountForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserAccountForm()

    return render(request, 'create_account.html', {'form': form})
