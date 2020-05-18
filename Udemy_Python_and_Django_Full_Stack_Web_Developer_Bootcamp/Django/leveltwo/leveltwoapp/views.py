from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from leveltwoapp.models import Topic, Webpage, AccessRecord

"""
def index(request):
    return HttpResponse("<h1>Hello, world. You're at the polls index.</h1>")

"""
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}

    template = loader.get_template('leveltwoapp/index.html')
    context = {
        'variable': 'from index.html',
    }
    return HttpResponse(template.render(date_dict, request))
# Create your views here.
