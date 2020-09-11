from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class SignupView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('profile')
    template_name = 'signup.html'

class AccountView(TemplateView):
    template_name = 'profile.html'
    