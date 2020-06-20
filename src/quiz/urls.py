from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('quiz/', views.home, name='home-page'),
    path('categories/', views.categories_page, name='categories'),
    path('quiz/create/', views.create_quiz, name='create-quiz')
]
