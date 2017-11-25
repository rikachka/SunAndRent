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
    owner = Customer.objects.get(pk=CUSTOMER_INDEX)
    items = StoragedGood.objects.filter(good_id__status='0').filter(good_id__owner_id=owner)
    template = loader.get_template('things/catalogue_stored.html')
    return HttpResponse(template.render({'stored_items' : items}, request))


def catalogue_rented(request):
    customer = Customer.objects.get(pk=CUSTOMER_INDEX)
    items = Reservation.objects.filter(customer_id=customer)
    template = loader.get_template('things/catalogue_rented.html')
    return HttpResponse(template.render({'rented_items' : items}, request))


def catalogue_goods(request):
    items = Good.objects.all()
    template = loader.get_template('things/catalogue_goods.html')
    return HttpResponse(template.render({'good_items' : items}, request))


def search_items(request):
    search_query = 'knife'
    items = Good.objects.filter(good_info__contains=search_query)
    template = loader.get_template('things/catalogue_goods.html')
    return HttpResponse(template.render({'good_items' : items}, request))


def return_good_to_owner(request, item_pk):
    good = Good.objects.get(pk=item_pk).update(status='1')
    return HttpResponseRedirect(reverse('catalogue_stored'))


def reset_status(request):
    owner = Customer.objects.get(pk=CUSTOMER_INDEX)
    Good.objects.filter(owner_id=owner).update(status='0')
    return HttpResponse("Status set to 'At service'")
