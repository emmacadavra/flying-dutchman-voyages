from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    # return HttpResponse("Home Page")
    return render(request, 'index.html')


def booking(request):
    # return HttpResponse("Booking Page")
    return render(request, 'booking.html')


def contact(request):
    # return HttpResponse("Contact Page")
    return render(request, 'contact.html')
