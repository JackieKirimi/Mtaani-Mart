from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def productStore(request):
    return HttpResponse("Welcome to our number one Product Store")
