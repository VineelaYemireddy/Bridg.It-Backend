from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    #return HttpResponse("HTML Tem will add here...... for Companies")
    return render(request, 'Company/index.html')

def companies(request):
    return HttpResponse("HTML Tem will add here...... for Company/products")