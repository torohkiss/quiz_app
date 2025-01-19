from django.db import models


# Create your models here.


class Question(models.Model):
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.text


class Answers(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    correct_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.text
