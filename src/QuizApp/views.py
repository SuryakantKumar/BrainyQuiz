from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    template = 'home.html'
    context = {'title': 'Home Page'}
    return render(request, template, context)


def about(request):
    template = 'about.html'
    context = {'title': 'About Us'}
    return render(request, template, context)


def contact(request):
    template = 'contact.html'
    context = {'title': 'Contact Us'}
    return render(request, template, context)
