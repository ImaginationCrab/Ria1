from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.


def landing(request):
    template = loader.get_template("movielibrary/landing.html")
    return render(request, "movielibrary/landing.html")

def registration(request):
    template = loader.get_template("movielibrary/registration.html")
    return render(request, "movielibrary/registration.html")

def login(request):
    template = loader.get_template("movielibrary/login.html")
    return render(request, "movielibrary/login.html")

def logout(request):
    return HttpResponse("Yo dis the logout page")

def home(request):
    return HttpResponse("Yo dis the home page")
