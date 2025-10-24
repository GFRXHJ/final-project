from django.shortcuts import render

def home_page(request):
    """Render home page"""
    return render(request, 'home.html')

def docs_page(request):
    """Render home page"""
    return render(request, 'docs.html')

def login_page(request):
    """Render login page"""
    return render(request, 'login.html')

def register_page(request):
    """Render register page"""
    return render(request, 'register.html')

def profile_page(request):
    """Render profile page"""
    return render(request, 'profile.html')

def forgot_password_page(request):
    """Render forgot password page"""
    return render(request, 'forgot_password.html')