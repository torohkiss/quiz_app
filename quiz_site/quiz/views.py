from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Choice
from .forms import QuestionForm, LoginForm

# Create your views here.

@login_required
def dashboard(request):
    return render(
        request,
        'quiz/dashboard.html',
        {'section': 'dashboard'}
    )

"""def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                    request,
                    username=cd['username'],
                    password=cd['password'],
                )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'quiz/login.html', {'form': form})"""



def quiz_home(request):
    return render(request, 'quiz/quiz_home.html')

def all(request):
    questions = Question.objects.all()

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            results = []
            total_correct = 0

            for field_name, choice_id in form.cleaned_data.items():
                question_id = int(field_name.split('_')[1])
                question = Question.objects.get(id=question_id)
                choice = Choice.objects.get(id=choice_id)
                is_correct = choice.correct_answer

                if is_correct:
                    total_correct += 1

                results.append({
                    'question': question,
                    'selected_choice': choice.text,
                    'is_correct': is_correct
                })
            return render(
                    request,
                    'quiz/result.html',
                    {
                        'results': results,
                        'total_correct': total_correct,
                        'total_questions': questions.count(),
                    }
                )
    else:
        form = QuestionForm()

    return render(
            request,
            'quiz/all_questions.html',
            {
                'form': form,
                'questions': questions,
            }
        )
