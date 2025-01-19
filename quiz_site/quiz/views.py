from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from .forms import QuestionForm

# Create your views here.

def question_view(request):
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
