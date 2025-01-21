from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Choice
from .forms import QuestionForm

# Create your views here.

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
