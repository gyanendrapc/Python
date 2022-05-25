from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

from .forms import UserDetailsForm


def home(requrest):
    return render(requrest, 'index.html')

def adduser(request):
    form = UserDetailsForm()
    return render(request, 'adduser.html',{'form':form})

def allnotes(request):
    return render(request, 'index.html')

def categories(request):
    return render(request, 'index.html')

def important(request):
    return render(request, 'index.html')


def login(requrest):
    pass

def logout(request):
    pass
