from django.urls import path
from . import views

urlpatterns = [
    path('welcome/',views.welcome,name = "welcome"),
    path('result/',views.result,name='result'),
    path('question',views.question,name='question')
]