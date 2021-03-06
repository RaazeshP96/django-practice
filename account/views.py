from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class SignupPageView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


