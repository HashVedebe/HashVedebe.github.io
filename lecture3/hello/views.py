from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, World")

def hilde(request):
    return HttpResponse("Hello Hilde")