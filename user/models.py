from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    question_text = models.CharField(max_length=512)
    choices = models.JSONField()  
    correct_answer = models.CharField(max_length=256)
    question_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_at[20]

class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    score_value = models.IntegerField(blank=True, null=True)
    scored_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username



