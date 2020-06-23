from django import forms

from .models import Quiz, Question, Option


class CreateQuizModelForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'description', 'difficulty', 'category']

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        qs = Quiz.objects.filter(title__iexact=title)
        if qs.exists():
            raise forms.ValidationError("This title is already exists. Please Choose a different one.")
        return title


class CreateQuestionModelForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'answer']


class AddOptionModelForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ['question', 'title', 'correctness']
