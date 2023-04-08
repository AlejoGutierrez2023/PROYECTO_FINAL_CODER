from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import ExtendedUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm, ProfileForm
from .models import Profile
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import make_password
from django.urls import reverse
from urllib.parse import urlencode
from django.http import HttpResponseRedirect


def base(request):
    return render(request, 'base.html')

def signup(request):
    if request.method == 'POST':
        user_form = ExtendedUserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.password = make_password(user_form.cleaned_data['password1'])
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.email = user_form.cleaned_data['email']
            profile.save()
            print(user_form.cleaned_data)
            print(profile_form.cleaned_data)
            login_url = reverse('login')
            return redirect(login_url)
    else:
        user_form = ExtendedUserCreationForm()
        profile_form = ProfileForm()
    return render(request, 'App_Accounts/signup.html', {'user_form': user_form, 'profile_form': profile_form})




def user_login(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and check_password(password, user.password):
                login(request, user)
                query_string = urlencode({'mensaje': f'Bienvenido {username}'})
                url = reverse('base') + '?' + query_string
                return HttpResponseRedirect(url)
            else:
                return render(request, 'App_Accounts/login_error.html', {'mensaje':f"Datos Incorrectos"})
            
        else:
            return render(request, 'App_Accounts/login_error.html', {'mensaje':f"Formulario Incorrecto"}) 
    form = AuthenticationForm()
    return render(request, 'App_Accounts/login.html', {'form':form} )

@login_required
def profile_view(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'App_Accounts/profile_detail.html', {'profile': profile})


@login_required
def edit_profile_view(request, pk):
    profile = get_object_or_404(Profile, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu perfil ha sido actualizado correctamente')
            return redirect('profile')

    else:
        form = ProfileForm(instance=profile)

    return render(request, 'App_Accounts/profile_edit.html', {'form': form})

@login_required
def delete_profile_view(request, pk):
    profile = get_object_or_404(Profile, pk=pk, user=request.user)
    if request.method == 'POST':
        profile.delete()
        messages.success(request, 'Tu perfil ha sido eliminado correctamente')
        return redirect('signup')
    return render(request, 'App_Accounts/profile_confirm_delete.html', {'profile': profile})