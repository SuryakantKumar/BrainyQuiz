from django.db import models
from django.conf import settings

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

    title = models.CharField(max_length=40)
    description = models.TextField(max_length=1000, blank=True, null=True)
    average_score = models.IntegerField(default=0, blank=True, null=True)
    Difficulty = models.CharField(max_length=1, choices=difficulty_choices, default='F')
    user_id = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.title


class Question(models.Model):
    title = models.CharField(max_length=400, blank=False, null=False)
    answer = models.CharField(max_length=400, blank=False, null=False)
    quiz_id = models.ForeignKey(Quiz, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.title


class Option(models.Model):
    title = models.CharField(max_length=400, blank=False, null=False)
    correctness = models.BooleanField(default=False, null=False)
    question_id = models.ForeignKey(Question, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.title


class QuestionWiseQuizScore(models.Model):
    per_question_score = models.IntegerField(default=0)
    quiz_id = models.ForeignKey(Quiz, null=False, blank=False, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '%s > %s > %s' % (self.question_id, self.per_question_score, self.user_id)


class Scoreboard(models.Model):
    score = models.IntegerField(default=0)
    quiz_id = models.ForeignKey(Quiz, null=False, blank=False, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '%s > %s > %s' % (self.user_id, self.quiz_id, self.score)
