from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.


def landing(request):
    template = loader.get_template("movielibrary/landing.html")
    return render(request, "movielibrary/landing.html")

def registration(request):
    return HttpResponse("Yo dis the registration page")

def login(request):
    return HttpResponse("Yo dis the login page")

def logout(request):
    return HttpResponse("Yo dis the logout page")

def home(request):
    return HttpResponse("Yo dis the home page")
