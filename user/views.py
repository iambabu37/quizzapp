from django.shortcuts import render

# Create your views here.

def welcome(request):
    return render(request,'user/welcome.html') 

def result(request):
    return render(request,'user/resultpage.html')

def question(request):
    return render (request,'user/question.html')