from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


def home(request):
    context = {'first':"Welcome to HOMEPAGE!"}
    return render(request, 'main/home.html', context)

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            pass_word = form.cleaned_data.get('password')

            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                messages.success(request, f"You are logged in successfully as {user_name.title()}")
                return redirect('post:categories')
            
            else:
                return HttpResponse('User is not activate!')
        
        else:
            return HttpResponse('Invalid username or password!')
    
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {
                                        'form':form,
                                    })

def user_logout(request):
    logout(request)
    messages.success(request, f"You are logged out!")
    return redirect('post:categories')

def registration(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        UserCreationForm()

        if form.is_valid():
            username = form.cleaned_data.get('username')
            saved_form = form.save()
            login(request, saved_form)
            messages.success(request, f"Successfully register as {username.title()}")
            return redirect('post:list')

        else:
            return HttpResponse('Invalid username or password!')
        
    else:
        form = UserCreationForm()
        return render(request, 'main/registration.html', {
                                            "form":form,
                                        })


