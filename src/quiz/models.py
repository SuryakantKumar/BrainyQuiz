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

    class Meta:
        ordering = ['title']


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

    class Meta:
        ordering = ['-date_posted']


class Question(models.Model):
    title = models.CharField(max_length=400, blank=False, null=False)
    answer = models.CharField(max_length=400, blank=False, null=False)
    quiz = models.ForeignKey(Quiz, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Option(models.Model):
    title = models.CharField(max_length=400, blank=False, null=False)
    correctness = models.BooleanField(default=False, null=False)
    question = models.ForeignKey(Question, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.title


class QuestionWiseQuizScore(models.Model):
    per_question_score = models.IntegerField(default=0)
    answer_triggered = models.CharField(null=True, blank=True, max_length=400)
    quiz_id = models.ForeignKey(Quiz, null=False, blank=False, on_delete=models.CASCADE)
    player = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '%s  %s  %s' % (self.question, self.per_question_score, self.player)


class QuizWiseScore(models.Model):
    per_quiz_score = models.IntegerField(default=0)
    quiz = models.ForeignKey(Quiz, null=False, blank=False, on_delete=models.CASCADE)
    player = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '%s  %s  %s' % (self.quiz, self.player, self.per_quiz_score)


class Scoreboard(models.Model):
    score = models.IntegerField(default=0)
    player = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '%s > %s' % (self.player, self.score)

    class Meta:
        ordering = ['-score']
