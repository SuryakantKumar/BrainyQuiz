from django import forms

from .models import Quiz, Question, Option, QuestionWiseQuizScore


class CreateQuizModelForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['category', 'title', 'description', 'difficulty']

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        qs = Quiz.objects.filter(title__iexact=title)
        if qs.exists():
            raise forms.ValidationError("This title is already exists. Please Choose a different one.")
        return title


class CreateQuestionModelForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title']


class CreateOptionModelForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ['title', 'correctness']
