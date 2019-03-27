from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.

def index(request):
    return HttpResponse("This is Index Page.")

def login(request):
    return HttpResponse("This is Login Page.")

def register(request):
    return HttpResponse("This is Register Page.")

def home(request):
    return HttpResponse("This is home page.")
