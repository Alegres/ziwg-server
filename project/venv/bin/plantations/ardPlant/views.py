from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import  authenticate
from django.contrib.auth import login
from .forms import SignUpForm,CustomPasswordChangeForm
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import EmailChangeForm
from django.contrib.auth import logout
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():

            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'home.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def profile(request):
    user = CustomUser.objects.filter(user=request.user)
    trueUser = user[0]
    return render(request, 'profile.html', {'userProfile':trueUser})

def changeData(request):


       if request.method == 'POST':
            if('changePassword' in request.POST):
                form = CustomPasswordChangeForm(request.user, request.POST)
                if form.is_valid():
                    user = form.save()
                    update_session_auth_hash(request, user)
                    messages.success(request, 'Password has been changed')
                    return redirect('changeData')
                else:
                 messages.error(request, 'There are errors in your form')
                 return redirect('changeData')
            if('changeEmail' in request.POST):
                form= EmailChangeForm(request.POST)
                if form.is_valid():
                    k=request.user
                    user = User.objects.filter(id=request.user.id)
                    changedUser=user[0]
                    if( changedUser.email !=request.POST.get('new_email1')  and request.POST.get('new_email1') == request.POST.get('new_email2') ):
                        changedUser.email=request.POST.get('new_email1')
                        changedUser.save()
                        messages.success(request, 'Email has been changed')
                    else:
                        messages.error(request, 'There are errors in your form!')
                    return redirect('changeData')
                else:
                 messages.error(request, 'There are errors in your form')
                 return redirect('changeData')
       else:
            form = CustomPasswordChangeForm(request.user)
            emailForm=EmailChangeForm()
            return render(request, 'changeData.html', {'form': form, 'form1':emailForm })
       return render(request,'changeData.html')