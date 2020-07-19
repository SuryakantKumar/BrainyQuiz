from django.urls import path

from . import views

urlpatterns = [
    path('', views.quiz_list_view, name='home-page'),
    path('category/', views.category_list_view, name='category-list'),
    path('category/<int:category_id>/', views.category_detail_view, name='category-detail'),
    path('quiz/', views.quiz_list_view, name='quiz-list'),
    path('quiz/create/', views.quiz_create_view, name='quiz-create'),
    path('quiz/<int:quiz_id>/view/', views.question_features_ext_view, name='question-feature-ext'),
    path('quiz/<int:quiz_id>/play/', views.quiz_play_view, name='quiz-play'),
    path('quiz/<int:quiz_id>/question/create/', views.question_create_view, name='question-create'),
    path('quiz/<int:quiz_id>/question/<int:question_id>/option/create/', views.option_create_view,
         name='option-create'),
    path('scoreboard/', views.score_board, name='scoreboard'),
    path('quiz/<int:quiz_id>/result/', views.quiz_result_view, name='quiz-result'),
    path('profile/download_content', views.download_content_view, name='download-content')
]
