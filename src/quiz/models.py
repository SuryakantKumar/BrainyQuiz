from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse

User = settings.AUTH_USER_MODEL


class Category(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return '%s' % self.title


class Quiz(models.Model):
    difficulty_choices = [
        ('H', 'Hard'),
        ('M', 'Medium'),
        ('E', 'Easy')
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, blank=True, null=True)
    average_score = models.IntegerField(default=0, blank=True, null=True)
    difficulty = models.CharField(max_length=10, choices=difficulty_choices, default='F')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('quiz-detail', kwargs={'pk': self.pk})


class Question(models.Model):
    title = models.CharField(max_length=400, blank=False, null=False)
    answer = models.CharField(max_length=400, blank=False, null=False)
    quiz = models.ForeignKey(Quiz, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return reverse('question-detail', kwargs={'pk': self.pk})


class Option(models.Model):
    title = models.CharField(max_length=400, blank=False, null=False)
    correctness = models.BooleanField(default=False, null=False)
    question = models.ForeignKey(Question, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.title


class QuestionWiseQuizScore(models.Model):
    per_question_score = models.IntegerField(default=0)
    quiz_id = models.ForeignKey(Quiz, null=False, blank=False, on_delete=models.CASCADE)
    player = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '%s > %s > %s' % (self.question, self.per_question_score, self.player)


class Scoreboard(models.Model):
    score = models.IntegerField(default=0)
    quiz = models.ForeignKey(Quiz, null=False, blank=False, on_delete=models.CASCADE)
    player = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '%s > %s > %s' % (self.player, self.quiz, self.score)
