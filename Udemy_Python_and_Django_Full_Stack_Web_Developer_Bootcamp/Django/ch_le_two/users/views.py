from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from users.models import User
from users.forms import NewUserForm

def index(request):
    return render(request, 'users/index.html')

#def users(request):
#    user_list = User.objects.order_by('first_name')
#    user_dict = {'users': user_list}
#    return render(request, 'users/users.html', context= user_dict)

def users(request):

    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR FORM INVALID")
    return render(request, "users/users.html",{"form":form})
