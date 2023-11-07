from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return HttpResponse("Home Page")


def booking(request):
    return HttpResponse("Booking Page")


def contact(request):
    return HttpResponse("Contact Page")