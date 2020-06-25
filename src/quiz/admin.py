from django.contrib import admin

from .models import Category, Quiz, Question, Option, QuestionWiseQuizScore, QuizWiseScore, Scoreboard

admin.site.register(Category)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(QuestionWiseQuizScore)
admin.site.register(QuizWiseScore)
admin.site.register(Scoreboard)
