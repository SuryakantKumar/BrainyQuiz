from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    template = 'about.html'
    context = {'title': 'QuizApp - About Us'}
    return render(request, template, context)


def contact(request):
    template = 'contact.html'
    context = {'title': 'QuizApp - Contact Us'}
    return render(request, template, context)
