from django.http import HttpResponse
from django.shortcuts import render

from quiz.models import Quiz, Question


def home(request):
    obj = Quiz.objects.all()
    # no_of_questions_per_quiz = {}
    # for each_quiz in obj:
    #     if each_quiz not in no_of_questions_per_quiz:
    #         each_quiz_title = each_quiz.title
    #         question_count_per_quiz = Question.objects.filter(quiz_id__title=each_quiz_title).count()
    #         no_of_questions_per_quiz[each_quiz_title] = question_count_per_quiz

    template = 'home.html'
    context = {'title': 'QuizApp - Home',
               "quizzes": obj}
    return render(request, template, context)


def about(request):
    template = 'about.html'
    context = {'title': 'QuizApp - About Us'}
    return render(request, template, context)


def contact(request):
    template = 'contact.html'
    context = {'title': 'QuizApp - Contact Us'}
    return render(request, template, context)
