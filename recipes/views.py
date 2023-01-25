from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, "recipes/index.html")


def about(request):
   return render(request, "recipes/about.html")


def exit_(request):
    return render(request, "recipes/exit.html")


def user(request):
    return HttpResponse("User password")

