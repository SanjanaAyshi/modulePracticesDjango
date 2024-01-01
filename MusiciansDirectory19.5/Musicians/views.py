from django.shortcuts import render, redirect
from . import forms
# Create your views here.
from . import models
from Albums.models import Album
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


# def addMusician(request):
#     if request.method == 'POST':
#         musiciansForm = forms.MusiciansFrom(request.POST)
#         if musiciansForm.is_valid():
#             musiciansForm.save()
#             return redirect('add_Musician')

#     else:
#         musiciansForm = forms.MusiciansFrom()
#     return render(request, 'addMusicians.html', {'form':  musiciansForm})


def edit_MU(request, id):
    musician = models.Musicians.objects.get(pk=id)
    musiciansForm = forms.MusiciansFrom(instance=musician)
    if request.method == 'POST':
        musiciansForm = forms.MusiciansFrom(request.POST, instance=musician)
        if musiciansForm.is_valid():
            musiciansForm.save()
            return redirect('homepage')

    return render(request, 'addMusicians.html', {'form': musiciansForm})


def register(request):
    if request.method == 'POST':
        registerForm = forms.RegistrationForm(request.POST)
        if registerForm.is_valid():
            registerForm.save()
            messages.success(request, 'Acount is created!! NICE!!')
            return redirect('register')

    else:
        registerForm = forms.RegistrationForm()
    return render(request, 'register.html', {'form': registerForm, 'type': 'Register'})


# login using class base
class UserLoginView(LoginView):
    template_name = 'register.html'
    # success_url = reverse_lazy('profile')

    def get_success_url(self):
        return reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Acount is logged In!! Ola Amigo!!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(
            self.request, 'Buddy!! Login information is not correct')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context


# @login_required
# def profile(request):
#     data = Album.objects.filter(musician=request.user)
#     return render(request, 'home.html', {'data': data})
