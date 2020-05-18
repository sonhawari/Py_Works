from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('leveltwoapp/index.html')
    context = {
        'help_insert': 'help me please',
    }
    return HttpResponse(template.render(context, request))
