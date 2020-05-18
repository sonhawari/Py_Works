from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from users.models import User

def index(request):
    return render(request, 'users/index.html')

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render(request, 'users/users.html', context= user_dict)
