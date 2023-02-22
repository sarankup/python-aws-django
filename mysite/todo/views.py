from django.http import HttpResponse
from django.shortcuts import render
import datetime


def index(request):
    friends = [ { "today": datetime.datetime.now(), "name": "Sara", "age": 40, "dob": "01-01-2020" }, { "today": datetime.datetime.now(), "name": "Karan", "age": 25, "dob": "02-01-2020" }]
    return render(request, "todo.html", {"friends": friends })

def add(request):
    context = { "total": (int(request.GET["a"])+int(request.GET["b"])) }
    return render(request, "math.html", context)

def home(request):
    return HttpResponse("You are seeing the home controller")



def hello(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def karan(request):
    return HttpResponse("Hello Karan")