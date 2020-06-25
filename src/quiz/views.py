from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from .models import Quiz, Category, Question, Option, QuestionWiseQuizScore, QuizWiseScore, Scoreboard
from .forms import CreateQuizModelForm, CreateQuestionModelForm, CreateOptionModelForm


def category_list_view(request):
    """ Function to retrieve all the Categories """
    objects = Category.objects.all()

    template = 'quiz/category_list.html'
    context = {"title": 'QuizApp - Categories',
               "categories": objects}
    return render(request, template, context)


def category_detail_view(request, category_id):
    objects = Quiz.objects.filter(category__id=category_id)

    template_name = 'quiz/category_detail.html'
    context = {"related_quiz": objects}
    return render(request, template_name, context)


def quiz_list_view(request):
    obj = Quiz.objects.all()

    template = 'quiz/home.html'
    context = {'title': 'QuizApp - Home',
               "quiz_list": obj}
    return render(request, template, context)


@login_required
def quiz_create_view(request):
    form = CreateQuizModelForm(request.POST or None)
    form.instance.author = request.user
    if form.is_valid():
        form.save()
        messages.success(request, f"Your Quiz has been added.")
        form = CreateQuizModelForm()

    template_name = 'quiz/quiz_create.html'
    context = {"title": "Create New Quiz",
               "form": form}
    return render(request, template_name, context)


@login_required
def question_create_view(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    if request.user != quiz.author:
        return redirect('/')
    form = CreateQuestionModelForm(request.POST or None)
    form.instance.quiz = quiz
    if form.is_valid():
        form.save()
        messages.success(request, f"Your Quiz has been added.")
        form = CreateQuestionModelForm()

    template_name = 'quiz/question_create.html'
    context = {"title": "Create New Question",
               "form": form,
               "related_quiz": quiz}
    return render(request, template_name, context)


def question_features_ext_view(request, quiz_id):
    quiz_object = get_object_or_404(Quiz, pk=quiz_id)
    question_objects = Question.objects.filter(quiz__id=quiz_id)
    option_objects = Option.objects.filter(question__quiz__id=quiz_id)

    template = 'quiz/question_feature_ext.html'
    context = {"question_list": question_objects,
               "related_quiz": quiz_object,
               "option_list": option_objects}
    return render(request, template, context)


def option_create_view(request, quiz_id, question_id):
    quiz_object = get_object_or_404(Quiz, pk=quiz_id)
    question_object = get_object_or_404(Question, pk=question_id)
    option_objects = Option.objects.filter(question__id=question_id)

    form = CreateOptionModelForm(request.POST or None)
    form.instance.question = question_object

    if form.is_valid():
        form.save()
        messages.success(request, f"Your Options has been added.")
        if option_objects.count() < 4:
            form = CreateOptionModelForm()
        else:
            return redirect('/quiz/')

    template_name = 'quiz/option_create.html'
    context = {"form": form,
               "question": question_object,
               "related_quiz": quiz_object,
               "option_list": option_objects}
    return render(request, template_name, context)


@login_required
def quiz_play_view(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)

    if QuizWiseScore.objects.filter(player=request.user, quiz=quiz_id).count() != 0:
        messages.success(request, f"You have already played selected quiz. Play other quiz.")
        return redirect('/')
    if request.method == 'POST':
        per_quiz_score = 0
        for question in quiz.question_set.all():
            player = request.user

            correct_option = None  # correct option of the question
            for option in question.option_set.all():
                if option.correctness is True:
                    correct_option = option

            option_triggered = False  # whether option is triggered or not
            option_triggered_value = None
            name_combination = str(quiz.id) + str(question.id)
            if request.POST.get(name_combination) is not None:
                option_triggered = True
                option_triggered_value = request.POST.get(name_combination)

            per_question_score = 0
            if (option_triggered is True) and (correct_option.title == option_triggered_value):
                per_question_score = 1
                per_quiz_score += 1

            question_wise_score = QuestionWiseQuizScore(quiz_id=quiz, player=player, question=question,
                                                        per_question_score=per_question_score)
            question_wise_score.save()

        quiz_wise_score = QuizWiseScore(per_quiz_score=per_quiz_score, quiz=quiz, player=request.user)
        quiz_wise_score.save()

        try:
            score_board_instance = get_object_or_404(Scoreboard, player=request.user)
            score_board_instance.score += per_quiz_score
            score_board_instance.save()
        except:
            new_board = Scoreboard(player=request.user, score=per_quiz_score)
            new_board.save()

        return redirect('/')

    template = 'quiz/quiz_play.html'
    context = {"related_quiz": quiz}
    return render(request, template, context)


def score_board(request):
    scoreboard = Scoreboard.objects.all()

    template = "quiz/scoreboard.html"
    context = {"scoreboard": scoreboard}
    return render(request, template, context)
