from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1> Welcome to home page, Juan Vera 111 </h1>')
# Create your views here.
