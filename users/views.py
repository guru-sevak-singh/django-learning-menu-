from django.forms import BaseModelForm
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm
from django.conf import settings
import os
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your views here.
class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        messages.success(self.request, f'Welcome {username}, Your Welcome in Our Site')
        return super().form_valid(form)
    

@login_required
def profile_page(request):
    return render(request, 'users/profile.html')
