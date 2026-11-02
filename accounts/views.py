from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Register View
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        confirm_password = request.POST.get('confirm_password', '').strip()

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, 'accounts/register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return render(request, 'accounts/register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "An account with this email already exists!")
            return render(request, 'accounts/register.html')

        # Create new user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, f"Account created for {username}! Please login.")
        return redirect('login')

    return render(request, 'accounts/register.html')


# Login View
def login_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        actual_username = user_input

        # Check if user entered an email address
        if '@' in user_input:
            user_obj = User.objects.filter(email__iexact=user_input).first()
            if user_obj:
                actual_username = user_obj.username
            else:
                actual_username = None

        user = authenticate(request, username=actual_username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('home')
        else:
            messages.error(request, "Account not found or invalid credentials. Please register first.")
            return render(request, 'accounts/login.html')

    return render(request, 'accounts/login.html')