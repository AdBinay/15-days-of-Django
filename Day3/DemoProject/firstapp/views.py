from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound

# Create your views here.

def home(request):
    print("home view is called")
    return HttpResponse("<h1>This is Home page</h1>", status = 200)