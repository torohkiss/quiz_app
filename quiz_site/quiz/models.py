from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Question(models.Model):
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=100)
    correct_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class UserScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    total_questions = models.IntegerField(default=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.user.username} - Score: {self.score} - {self.timestamp}"
