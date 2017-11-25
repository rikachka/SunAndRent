from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def catalogues(request):
    template = loader.get_template('things/catalogues.html')
    context = {}
    return HttpResponse(template.render(context, request))

def catalogue_stored(request):
    template = loader.get_template('things/catalogue_stored.html')
    context = {}
    return HttpResponse(template.render(context, request))

def index2(request):
    return HttpResponse("Hello, world. You're at the index2.")