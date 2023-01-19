from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(response):
    return HttpResponse("<h1>Hello, World!</h1>")

def v1(response):
    return HttpResponse("<h1>Hello, World! v1</h1><style>body {background-color: #222222;}</style>")