from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login as auth_login,logout
from user.models import *

def signup(request):
    if request.method == "POST":
        # Collect form data
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("repassword")

        # Comprehensive Validation
        if not all([name, email, password, confirm_password]):
            messages.error(request, "All fields are required")
            return render(request, 'signup.html')

        # Password Matching Validation
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return render(request, 'signup.html')

        # Password Strength Validation
        if len(password) < 8:
            messages.error(request, "Password must be at least 8 characters long")
            return render(request, 'signup.html')

        # Username Uniqueness Check
        if User.objects.filter(username=name).exists():
            messages.error(request, "Username already exists")
            return render(request, 'signup.html')

        # Email Uniqueness Check
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return render(request, 'signup.html')

        try:
            # Create User with Secure Password
            new_user = User.objects.create_user(
                username=name,
                email=email,
                password=password  # Django will hash this automatically
            )
            print(f'user is created { new_user}')
            
            messages.success(request, "Account created successfully!")
            return redirect('login')

        except Exception as e:
            messages.error(request, f"Registration failed: {str(e)}")
            return render(request, 'signup.html')

    # GET Request
    return render(request, 'signup.html')


def login(request):
    if request.method == "POST":
        # Get username and password from form
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Validate input
        if not username or not password:
            messages.error(request, "Please enter both username and password")
            return render(request, 'login.html')

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Login successful
            auth_login(request, user)
            messages.success(request, "Login successful!")
            return redirect('quizlist')  # Replace with your homepage URL name
        else:
            # Login failed
            messages.error(request, "Invalid username or password")
            return render(request, 'login.html')

    # GET request - render login page
    return render(request, 'login.html')

def logoutuser(reqeust):
    messages.success(reqeust,'Log out successfully ')
    logout(reqeust)
    return redirect('login')


def quizlist(request):
    quizzes = Quiz.objects.all()
    return render(request,'quiz.html',{"quizzes":quizzes})
