from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import SignupForm, LoginForm

def index(request):
    return render(request, 'index.html')

def accountLogin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        response = {'form': form,}
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        response['not_valid'] = True
        return render(request, 'login.html', response)
    else:
        form = LoginForm()
    response = {
        'form': form,
    }
    return render(request, 'login.html', response)

def accountSignup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        response = {
            'form': form,
        }
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=name,
            )
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('index')
        response['not_valid'] = True
        return render(request, 'signup.html', response)
    else:
        form = SignupForm()
    response = {
        'form': form,
    }
    return render(request, 'signup.html', response)

def accountSignout(request):
    logout(request)
    return redirect('index')
