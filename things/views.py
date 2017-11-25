from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Good, Customer, StoragedGood

def catalogues(request):
    template = loader.get_template('things/catalogues.html')
    context = {}
    return HttpResponse(template.render(context, request))

def catalogue_stored(request):
    index = 1
    owner = Customer.objects.get(pk=index)
    items = StoragedGood.objects.filter(good_id__owner_id=owner)
    template = loader.get_template('things/catalogue_stored.html')
    return HttpResponse(template.render({'stored_items' : items}, request))


def catalogue_rented(request):
    index = 1
    owner = Customer.objects.get(pk=index)
    items = StoragedGood.objects.filter(good_id__owner_id=owner)
    template = loader.get_template('things/catalogue_stored.html')
    return HttpResponse(template.render({'rented_items' : items}, request))


def index2(request):
    return HttpResponse("Hello, world. You're at the index2.")

def get_stored_by_person_id(request):
    owner = Customer.objects.get(pk=request['id'])
    items = StoredGood.objects.filter(ownwer_id=owner)
    return items
