from django import forms

class QuestionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question')
        super().__init__(*args, **kwargs)
        self.fields['choices'] = forms.ChoiceField(
            label=question.text,
            choices=[(choice.id, choice.text) for choice in question.choices.all()],
            widget=forms.RadioSelect,
        )
