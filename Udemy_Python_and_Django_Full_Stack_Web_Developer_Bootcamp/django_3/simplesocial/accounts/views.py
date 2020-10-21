from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.genereic import CreateView
from . import forms
# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_ırl = reverse_lazy('login')
    template_name = 'accounts/signup.html'
