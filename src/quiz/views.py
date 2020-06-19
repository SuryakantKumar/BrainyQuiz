from django.shortcuts import render

from .models import Category


def categories_page(request):
    obj = Category.objects.all()
    template = 'categories.html'
    context = {"title": 'QuizApp - Categories',
               "categories": obj}
    return render(request, template, context)
