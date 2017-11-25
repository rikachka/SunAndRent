from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Good, Customer, StoragedGood, Reservation
from django.urls import reverse


CUSTOMER_INDEX = 1


def catalogues(request):
    template = loader.get_template('things/catalogues.html')
    context = {}
    return HttpResponse(template.render(context, request))


def catalogue_stored(request):
    # good = Good.objects.get(pk=1)
    # good.status = '0'
    # good.save()
    owner = Customer.objects.get(pk=CUSTOMER_INDEX)
    items = StoragedGood.objects.filter(good_id__status='0').filter(good_id__owner_id=owner)
    template = loader.get_template('things/catalogue_stored.html')
    return HttpResponse(template.render({'stored_items' : items}, request))


def catalogue_rented(request):
    customer = Customer.objects.get(pk=2)
    items = Reservation.objects.filter(customer_id=customer)
    template = loader.get_template('things/catalogue_rented.html')
    return HttpResponse(template.render({'rented_items' : items}, request))


def catalogue_goods(request):
    items = Good.objects.all()
    template = loader.get_template('things/catalogue_goods.html')
    return HttpResponse(template.render({'good_items' : items}, request))


def return_good_to_owner(request, item_pk):
    good = Good.objects.get(pk=item_pk)
    good.status = '1'
    good.save()
    return HttpResponseRedirect(reverse('catalogue_stored'))
