from django.urls import path
from . import views

urlpatterns = [
    path('welcome/<str:quiz_id>/',views.welcome,name = "welcome"),
    # path('result/',views.result,name='result'),
    # path('question/',views.question,name='question'),

    path('quiz/<int:quiz_id>/start/', views.start_quiz, name='quiz'),
    path('quiz/question/', views.quiz_question, name='quiz_question'),
    path('quiz/result/', views.quiz_result, name='quiz_result'),



    # path('quiz/<str:quiz_id>/',views.quiz,name = 'quiz')
]