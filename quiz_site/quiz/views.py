from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Choice
from .forms import QuestionForm

# Create your views here.

def all(request):
    #questions = Question.objects.all()
    questions = Question.objects.prefetch_related('choices').all()
    return render(
            request,
            'quiz/all_questions.html',
            {
                'questions': questions,
            }
        )

def submit_answers(request):
    if request.method == 'POST':
        results = {}
        for question in Question.objects.all():
            selected_choice_id = request.POST.get(f'question_{question.id}')
            if selected_choice_id:
                 selected_choice = Choice.objects.get(id=selected_choice_id)
                 results[question.id] = {
                    'question': question.text,
                    'selected': selected_choice.text,
                    'correct_answer': selected_choice.correct_answer
                }
        return render(request, 'quiz/results.html', {'results': results})
    return redirect('all_questions')

def question_view(request, question_id):
    question = get_object_or_404(Question, id=question_id)

    if request.method == 'POST':
        form = QuestionForm(request.POST, question=question)
        if form.is_valid():
            choice_id = form.cleaned_data['choices']
            choice = Choice.objects.get(id=choice_id)
            if choice.correct_answer:
                return render(request, 'quiz/result.html', {'result': 'Correct answer!'})
            else:
                return render(request, 'quiz/result.html', {'result': 'Wrong answer!'})

    else:
        form = QuestionForm(question=question)

    return render(request, 'quiz/question.html', {'form': form, 'question': question})
