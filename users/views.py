from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm
from quiz.models import Quiz


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Your account has been created. Now you can Login.")
            return redirect('/login')
    else:
        form = UserRegistrationForm()

    template = 'users/register.html'
    context = {"form": form,
               "title": 'Sign Up'}
    return render(request, template, context)


@login_required
def profile(request):
    quiz = Quiz.objects.filter(author=request.user).select_related('author')

    template = 'users/profile.html'
    context = {"title": 'Profile',
               "quiz_list": quiz}
    return render(request, template, context)
