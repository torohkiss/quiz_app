from django import forms
from .models import Question, Choice

"""class QuestionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question')
        super().__init__(*args, **kwargs)
        self.fields['choices'] = forms.ChoiceField(
            label=question.text,
            choices=[(choice.id, choice.text) for choice in question.choices.all()],
            widget=forms.RadioSelect,
        )"""


class QuestionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Getting all questions and creating the fields dynamically
        
        questions = Question.objects.all()
        for question in questions:
            field_name = f'question_{question.id}'
            choices = [(choice.id, choice.text) for choice in question.choices.all()]
            self.fields[field_name] = forms.ChoiceField(
                    label=question.text,
                    choices=choices,
                    widget=forms.RadioSelect,
                    required=True
                )
