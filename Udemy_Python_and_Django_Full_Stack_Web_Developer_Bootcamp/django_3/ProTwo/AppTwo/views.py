from django.shortcuts import render
from django.http import HttpResponse
#from AppTwo.models import User

from AppTwo.forms import NewUserForm
# Create your views here.
def index(request):
    return HttpResponse(" <em> My Second App </em>")

def help(request):
    tagme = { 'put_me':'Help Page' }
    return render(request, "AppTwo\help.html", context=tagme)


def user(request):

    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print("ERROR FORM INVALID")

    return render(request,'appTwo\\users.html', {'form':form} )
