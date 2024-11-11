from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def home(request):
    return render(request, 'user/index.html')





def signups(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        mobile_number = request.POST['mobile_number']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('signups')  # Redirect to the signup page/modal
        
        # Create a new signup record
        new_user = signup(
            username=username,
            email=email,
            mobile_number=mobile_number,
            password=password,
            confirm_password=confirm_password
        )
        new_user.save()

        messages.success(request, "Signup successful!")
        return redirect('login')  # Redirect to the home page or another page after signup
    
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Check if a user exists with the provided email
        try:
            user = signup.objects.get(email=email)
        except signup.DoesNotExist:
            messages.error(request, "No account exists with this email.")
            return redirect('login')

        # Verify the password
        if user.password == password:
            # Assuming user is authenticated, now log them in
            # Optionally, you can integrate Django's authentication system later
            messages.success(request, "Login successful!")
            return redirect('dashboard')  # Redirect to home page after successful login
        else:
            messages.error(request, "Invalid password.")
            return redirect('login')

    return render(request, 'user/login.html')

def dashboard(request):
    return render(request,'user/dashboard.html')
