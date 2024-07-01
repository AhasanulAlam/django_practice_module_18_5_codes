from django.shortcuts import render, redirect
from . forms import RegisterForm, ChangeUserDataForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request, 'User Account created successfully!')
                # messages.warning(request, 'Warning!')
                # messages.info(request, 'Info!')
                form.save()
                print(form.cleaned_data)
        else:
            form = RegisterForm()
        return render(request, './signup.html', {'form' : form})
    else:
        return redirect('profile_page')
    

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data = request.POST)
            if form.is_valid():
                uName = form.cleaned_data['username']
                uPass = form.cleaned_data['password']
                user = authenticate(username = uName, password = uPass) # check the user in in the database
                if user is not None:
                    login(request, user)
                    messages.success(request, 'User Logged In Successfully!')
                    return redirect('profile_page')
        else:
            form = AuthenticationForm()
        return render(request, './login.html', {'form' : form})
    else:
        return redirect('profile_page')

def user_logout(request):
    logout(request)
    messages.success(request, 'User Logged Out Successfully!')
    return redirect('login_page')

def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangeUserDataForm(request.POST, instance = request.user)
            if form.is_valid():
                messages.success(request, 'User Account Data update successfully!')
                form.save()
        else:
            form = ChangeUserDataForm(instance = request.user)
        return render(request, './profile.html', {'form' : form})
    else:
        return redirect('signup_page')
    

def pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)    #will do the password update
                messages.success(request, 'User Password changed successfully!')
                return redirect('profile_page')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, './passchange.html', {'form' : form})
    else:
        return redirect('login_page')


def pass_change_without_old(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)    #will do the password update
                messages.success(request, 'User Password changed successfully!')
                return redirect('profile_page')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, './passchange.html', {'form' : form})
    else:
        return redirect('login_page')


def change_user_data(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangeUserDataForm(request.POST, instance = request.user)
            if form.is_valid():
                messages.success(request, 'User Account Data update successfully!')
                form.save()
                print(form.cleaned_data)
        else:
            form = ChangeUserDataForm()
        return render(request, './profile.html', {'form' : form})
    else:
        return redirect('signup_page')
    
