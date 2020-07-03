from django.shortcuts import render

from .documents import QuizDocument, QuestionDocument


def search(request):
    q = request.GET.get('q')

    if q:
        quizzes = QuizDocument().search().query('match', title=q)
        questions = QuestionDocument().search().query('match', title=q)
    else:
        quizzes = ''
        questions = ''

    template = 'searches/search.html'
    context = {'quizzes': quizzes,
               'questions': questions,
               'query': q}
    return render(request, template, context)
