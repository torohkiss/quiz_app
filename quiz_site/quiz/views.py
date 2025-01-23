from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Choice, UserScore
from .forms import QuestionForm, LoginForm
from django.utils import timezone
from django.contrib import messages

# Create your views here.

@login_required
def dashboard(request):
    user_scores = UserScore.objects.filter(user=request.user).order_by('-timestamp')[:5]

    return render(
        request,
        'quiz/dashboard.html',
        {
            'section': 'dashboard',
            'user_scores': user_scores,
            'current_time': timezone.now().strftime('%Y-%m-%d %H:%M:%S'),
            'username': request.user.username,
        }
    )

@login_required
def reset_scores(request):
    if request.method == 'POST':
        UserScore.objects.filter(user=request.user).delete()
        messages.success(request, 'Your scores have been reset successfully!')
    return redirect('dashboard')

@login_required
def quiz_home(request):
    return render(request, 'quiz/quiz_home.html')


@login_required
def all(request):
    request.session['last_activity'] = timezone.now().isoformat()


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

            UserScore.objects.create(
                    user=request.user,
                    score=total_correct,
                    total_questions=questions.count()
                )

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

@login_required
def quiz_results(request):
    results = request.session.get('quiz_results', {})

    # Calculate the total correct answers
    correct_count = sum(1 for result in results.values() if result['is_correct'])

    # Save the score
    UserScore.objects.create(
        user=request.user,
        score=correct_count
    )

    return render(request, 'quiz/results.html', {'results': results})
