from django import forms
from .models import Question, Choice



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

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
