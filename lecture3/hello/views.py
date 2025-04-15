from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def hilde(request):
    return HttpResponse("Hello Hilde")

def manu(request):
    return HttpResponse("Dag Manu")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })