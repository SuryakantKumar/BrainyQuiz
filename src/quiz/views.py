from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView

from .models import Quiz, Category
from .forms import CreateQuizModelForm, AddQuestionModelForm, AddOptionModelForm


class QuizListView(ListView):
    model = Quiz
    template_name = 'quiz/home.html'
    context_object_name = 'quizzes'
    ordering = ['-date_posted']


class QuizDetailView(DetailView):
    model = Quiz
    template_name = 'quiz/quiz_detail.html'
    context_object_name = 'quiz'


class CategoryListView(ListView):
    model = Category
    template_name = 'quiz/category_list.html'
    context_object_name = 'categories'
    ordering = ['title']


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'quiz/category_detail.html'
    context_object_name = 'category'


# @login_required
# def create_quiz(request):
#     form = CreateQuizModelForm(request.POST or None)
#     form.instance.author = request.user
#     if form.is_valid():
#         form.save()
#         messages.success(request, f"Your Quiz has been added.")
#         form = CreateQuizModelForm()
#
#     template_name = 'quiz/create_quiz.html'
#     context = {"title": "Create New Quiz",
#                "form": form}
#     return render(request, template_name, context)


class QuizCreateView(LoginRequiredMixin, CreateView):
    model = Quiz
    fields = ['title', 'description', 'difficulty', 'category']
    template_name = 'quiz/create_quiz.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
