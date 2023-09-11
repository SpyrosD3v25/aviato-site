from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm
from django.contrib.auth import get_user_model

User = get_user_model()  # Get the User model you've defined

from django.contrib.auth import login, authenticate

def signup_view(request):
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user.set_password(raw_password)  # Hash the password
            user.role = User.NORMAL_USER  # Set the role to "Normal User"
            user.save()  # Save the user with hashed password
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/')  # Replace 'home' with the name of your home page URL
    else:
        form = UserRegistrationForm()
    return render(request, 'sign-up.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('')  # Replace 'home' with the name of your home page URL
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})