from django.urls import path

from . import views

urlpatterns = [
    path('', views.quiz_list_view, name='home-page'),
    path('category/', views.category_list_view, name='category-list'),
    path('category/<int:category_id>/', views.category_detail_view, name='category-detail'),
    path('quiz/', views.quiz_list_view, name='quiz-list'),
    path('quiz/create/', views.quiz_create_view, name='quiz-create'),
    path('quiz/<int:quiz_id>/play', views.question_list_view, name='question-list'),


    path('quiz/<int:quiz_id>/question/create', views.question_create_view, name='question-create')
]
