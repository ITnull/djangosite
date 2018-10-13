from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def welcome(request):
    return HttpResponse("<h1>welcome to my tiny twitter!</h1>")


