from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.

def welcome(request,quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)

    return render(request,'user/welcome.html',{'quiz':quiz}) 



# @login_required
def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz_list.html', {'quizzes': quizzes})

# @login_required
def start_quiz(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    questions = list(quiz.questions.all())[:5]
    
    # Create quiz attempt
    attempt = QuizAttempt.objects.create(
        user=request.user, 
        quiz=quiz,
        total_questions=len(questions)
    )
    
    # Store in session
    request.session['quiz_attempt_id'] = attempt.id
    request.session['questions'] = [q.id for q in questions]
    request.session['current_question_index'] = 0
    request.session['user_answers'] = {}
    
    return redirect('quiz_question')

# @login_required
def quiz_question(request):
    # Retrieve session data
    attempt_id = request.session.get('quiz_attempt_id')
    questions = request.session.get('questions', [])
    current_index = request.session.get('current_question_index', 0)
    
    # Check if quiz is complete
    if current_index >= len(questions):
        return redirect('quiz_result')
    
    # Get current question
    current_question_id = questions[current_index]
    question = Question.objects.get(id=current_question_id)
    options = question.options.all()
    print(options)
    
    if request.method == 'POST':
        selected_option_id = request.POST.get('option')
        
        # Store user's answer in session
        user_answers = request.session.get('user_answers', {})
        user_answers[str(current_question_id)] = selected_option_id
        request.session['user_answers'] = user_answers
        
        # Move to next question
        request.session['current_question_index'] += 1
        
        return redirect('quiz_question')
    
    context = {
        'question': question,
        'options': options,
        'current_question': current_index + 1,
        'total_questions': len(questions)
    }
    
    return render(request, 'user/quiz_question.html', context)

@login_required
def quiz_result(request):
    attempt_id = request.session.get('quiz_attempt_id')
    questions = request.session.get('questions', [])
    user_answers = request.session.get('user_answers', {})
    
    attempt = QuizAttempt.objects.get(id=attempt_id)
    score = 0
    detailed_results = []
    
    for question_id in questions:
        question = Question.objects.get(id=question_id)
        user_answer_id = user_answers.get(str(question_id))
        
        if user_answer_id:
            selected_option = Option.objects.get(id=user_answer_id)
            is_correct = selected_option.is_correct
            correct_answer = question.options.filter(is_correct=True).first().text
            user_answer_text = selected_option.text
        else:
            is_correct = False
            correct_answer = question.options.filter(is_correct=True).first().text
            user_answer_text = 'Not Answered'
        
        if is_correct:
            score += 1
        
        detailed_results.append({
            'question': question.text,
            'user_answer': user_answer_text,
            'correct_answer': correct_answer,
            'is_correct': is_correct
        })
    
    # Update attempt
    attempt.score = score
    attempt.completed = True
    attempt.save()
    
    # Clear session
    del request.session['quiz_attempt_id']
    del request.session['questions']
    del request.session['current_question_index']
    del request.session['user_answers']
    
    context = {
        'score': score,
        'total_questions': len(questions),
        'percentage': (score / len(questions)) * 100,
        'detailed_results': detailed_results
    }
    
    return render(request, 'user/quiz_result.html', context)








































































































# def result(request):
#     return render(request,'user/resultpage.html')

# def question(request):
#     questions = Question.objects.all()
#     data = {'questions': questions}
#     print(data)
#     return render (request,'user/question.html',data)




# def quiz(request ,quiz_id):
#     quiz = Quiz.objects.get(id=quiz_id)
#     questions = list(quiz.questions.all())
#     # options = list(questions.options.all())
#     print(questions)
#     # print(options)
#     attempt = QuizAttempt.objects.create(
#         user = request.user,
#         quiz = quiz,
#         score_value = len(questions)
#     )
#     return render(request,'user/question.html',{'questions' : questions})

    # request.session['quiz_attempt_id'] = attempt.id
    # request.session['questions'] = [q.id for q in questions]
    # request.session['current_question_index'] = 0
    # request.session['user_answers'] = {}

    # return redirect ('quiz')

