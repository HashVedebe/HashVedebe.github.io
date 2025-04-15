from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def hilde(request):
    return HttpResponse("Hello Hilde")

def manu(request):
    return HttpResponse("Dag Manu")

def greet(request, name):
    return HttpResponse(f"Hello {name.capitalize()}")