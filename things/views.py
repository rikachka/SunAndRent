from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Good, Customer, StoragedGood, Reservation
from django.urls import reverse
from django.utils import timezone
import datetime


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
    items = Good.objects.all().exclude(owner_id__exact=CUSTOMER_INDEX)
    template = loader.get_template('things/catalogue_goods.html')
    return HttpResponse(template.render({'good_items' : items}, request))


def search_items_rented(request):
    key_word = request.GET['search_field']
    customer = Customer.objects.get(pk=CUSTOMER_INDEX)
    items = Reservation.objects.filter(customer_id=customer).filter(good_id__good_info__contains=key_word)
    template = loader.get_template('things/catalogue_rented.html')
    return HttpResponse(template.render({'rented_items' : items}, request))


def search_items_stored(request):
    key_word = request.GET['search_field']
    owner = Customer.objects.get(pk=CUSTOMER_INDEX)
    items = StoragedGood.objects.filter(good_id__status='0').filter(good_id__owner_id=owner).filter(good_id__good_info__contains=key_word)
    template = loader.get_template('things/catalogue_stored.html')
    return HttpResponse(template.render({'stored_items' : items}, request))


def search_items_goods(request):
    key_word = request.GET['search_field']
    items = Good.objects.filter(good_info__contains=key_word)
    template = loader.get_template('things/catalogue_goods.html')
    return HttpResponse(template.render({'good_items' : items}, request))


def receive_back_item(request, item_pk):
    Good.objects.filter(pk=item_pk).update(status='1')
    return HttpResponseRedirect(reverse('catalogue_stored'))


def rent_item(request, item_pk):
    reservation = Reservation(start_date=timezone.now(),
                              end_date=timezone.now() + datetime.timedelta(7),
                              customer_id=Customer.objects.get(pk=CUSTOMER_INDEX),
                              good_id=Good.objects.get(pk=item_pk))
    reservation.save()
    return HttpResponseRedirect(reverse('catalogue_goods'))



def return_item(request, item_pk):
    Reservation.objects.filter(pk=item_pk).update(return_date=timezone.now())
    return HttpResponseRedirect(reverse('catalogue_rented'))


def reset_status(request):
    owner = Customer.objects.get(pk=CUSTOMER_INDEX)
    Good.objects.filter(owner_id=owner).update(status='0')
    return HttpResponse("Status set to 'At service'")


def item_stored_fullinfo(request, item_pk):
    item = StoragedGood.objects.get(pk=item_pk)
    template = loader.get_template('things/item_stored_fullinfo.html')
    return HttpResponse(template.render({'item' : item}, request))


def item_rented_fullinfo(request, item_pk):
    item = Reservation.objects.get(pk=item_pk)
    template = loader.get_template('things/item_rented_fullinfo.html')
    return HttpResponse(template.render({'item' : item}, request))


def item_good_fullinfo(request, item_pk):
    item = Good.objects.get(pk=item_pk)
    template = loader.get_template('things/item_good_fullinfo.html')
    return HttpResponse(template.render({'item' : item}, request))
