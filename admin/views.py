from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def jobs(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        

       
        
        # Create a new signup record
        new_user = jobs(
            username=username,
            email=email,
           
        )
        new_user.save()

        messages.success(request, "Signup successful!")
        return redirect('login')  # Redirect to the home page or another page after signup
    
    return render(request, 'admin_search.html')
