from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('things/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def index2(request):
    return HttpResponse("Hello, world. You're at the index2.")