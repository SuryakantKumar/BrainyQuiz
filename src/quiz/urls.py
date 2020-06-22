from django.urls import path

from .views import QuizListView, QuizDetailView, CategoryListView, CategoryDetailView, QuizCreateView
from . import views

urlpatterns = [
    path('', QuizListView.as_view(), name='Home'),
    path('quiz/', QuizListView.as_view(), name='quiz-list'),
    path('quiz/<int:pk>/', QuizDetailView.as_view(), name='quiz-detail'),
    path('category/', CategoryListView.as_view(), name='category-list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('quiz/create/', QuizCreateView.as_view(), name='create-quiz'),
    # path('quiz/create/', views.create_quiz, name='create-quiz'),
]
