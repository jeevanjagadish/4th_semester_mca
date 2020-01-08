from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<H2>Hi! Welcome to Reckonsys!</H2>')
    

# Create your views here.
