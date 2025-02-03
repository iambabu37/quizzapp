from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator ,MaxValueValidator


# class Quiz(models.Model):
#     title = models.CharField(max_length=256)
#     description = models.TextField(blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now = True)
#     total_questions = models.PositiveIntegerField(
#         default=10,
#         validators=[MinValueValidator(1)]
#     )
#     passing_score = models.FloatField(
#         default = 55.0,
#         validators=[
#             MinValueValidator(0),
#             MaxValueValidator(100)
#         ]
#     )

#     time_per_question = models.IntegerField(
#         default=120,
#         help_text='time limit for the each questions'
#     )
#     DIFFICULTY_LEVEL =  [
#         ("EASY",'easy'),
#         ("MEDIUM",'medium'),
#         ("HARD",'hard')
#     ]

#     difficulty = models.CharField(
#         max_length=10,
#         choices=DIFFICULTY_LEVEL,
#         default='MEDIUM'
#     )

#     def __str__(self):
#         return self.title
    
#     def get_total_questions(self):
#         return self.questions.count()
    
#     def calculate_total_time(self):
#         """calculating the total time of the quizz """
#         return self.time_per_question * self.total_questions
    



# class Question(models.Model):
#     quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE,related_name='questions')
#     text = models.TextField()
#     question_at = models.DateTimeField(auto_now_add=True)
#     marks = models.FloatField(default=1.0)

#     def __str__(self):
#         return f"{self.text[:50]}..." if len(self.text) > 50 else self.text


# class QuizAttempt(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     quiz = models.ForeignKey(Quiz , on_delete = models.CASCADE)  
#     score_value = models.IntegerField(blank=True, null=True)
#     scored_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.user.username

# class Option(models.Model):
#     question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name='options')
#     text = models.TextField()
#     is_correct = models.BooleanField(default=False)

#     def __self__(self):
#         return f"{self.text[:50]}..." if len(self.text) > 50 else self.text
    

from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'quiz'

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()
    
    def __str__(self):
        return self.text[:50]
    class Meta:
        db_table = 'question'

class Option(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    
    def __str__(self):
        return self.text
    class Meta:
        db_table = 'option'

class QuizAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    total_questions = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.quiz.title}"
