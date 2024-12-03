from django.shortcuts import render, redirect
from .forms import SignUpForm,LoginForm
from django.contrib.auth import logout
from django.contrib.auth import authenticate ,login as auth_login
from django.contrib import messages


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import SignUpForm
from django.contrib import messages

def register(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Get cleaned data from the form
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create_user(username=username, email=email, password=password)

            user.save()

            # Show success message
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('login')  # Redirect to the login page or other page

    return render(request, 'usermodule/register.html', {'form': form})



from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import LoginForm  # Assuming LoginForm is imported

def loginUser(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth_login(request, user)
                messages.success(request, f"Welcome, {username}!")
                return redirect('index')  # Redirect to home page or dashboard
            else:
                # Show error if authentication fails
                messages.error(request, "Invalid username or password.")
    return render(request, "usermodule/login.html", {'form': form})



def logoutUser(request):
    logout(request)
    return redirect('login')

