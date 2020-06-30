from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from register.models import Register_mdl
from register.forms import RegisterForm
from notebook.views import index

# Create your views here.
def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render( request, 'notebook/index.html')
        else:
            print("ERROR FORM INVALID")

    return render( request, 'register/register.html',{"form":form})
    #return HttpResponse("asdasd dads ")
