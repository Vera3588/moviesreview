from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    searchTerm = request.GET.get('searchMovie')
    return render(request,'home.html',{'searchTerm':searchTerm})
# Create your views here.
