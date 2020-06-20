from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Quiz, Category
from .forms import CreateQuizModelForm


def home(request):
    obj = Quiz.objects.all()

    template = 'home.html'
    context = {'title': 'QuizApp - Home',
               "quizzes": obj}

    return render(request, template, context)


def categories_page(request):
    obj = Category.objects.all()

    template = 'categories.html'
    context = {"title": 'QuizApp - Categories',
               "categories": obj}
    return render(request, template, context)


@login_required
def create_quiz(request):
    form = CreateQuizModelForm(request.POST or None)
    form.instance.author = request.user
    if form.is_valid():
        form.save()
        messages.success(request, f"Your Quiz has been added.")
        form = CreateQuizModelForm()

    template_name = 'quiz/create_quiz.html'
    context = {"title": "Create New Quiz",
               "form": form}
    return render(request, template_name, context)

