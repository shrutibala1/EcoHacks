from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm

def home(request):
    return render(request, 'users/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Redirect to a success page or do something else
            return redirect('/main')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})