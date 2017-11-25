from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^catalogue_goods$', views.catalogue_goods, name='catalogue_goods'),
    url(r'^catalogue_stored$', views.catalogue_stored, name='catalogue_stored'),
    url(r'^catalogue_rented$', views.catalogue_rented, name='catalogue_rented'),
    url(r'^receive_back_item/(?P<item_pk>[0-9]+)$', views.receive_back_item, name='receive_back_item'),
    url(r'^rent_item/(?P<item_pk>[0-9]+)$', views.rent_item, name='rent_item'),
    url(r'^search_rented$', views.search_items_rented, name='search_rented'),
    url(r'^search_stored$', views.search_items_stored, name='search_stored'),
    url(r'^search_goods$', views.search_items_goods, name='search_goods'),
    url(r'^item_stored/(?P<item_pk>[0-9]+)', views.item_stored_fullinfo, name='item_stored_fullinfo'),
    url(r'^item_rented/(?P<item_pk>[0-9]+)', views.item_rented_fullinfo, name='item_rented_fullinfo'),
    url(r'^item_good/(?P<item_pk>[0-9]+)', views.item_good_fullinfo, name='item_good_fullinfo'),
    url(r'^reset_status', views.reset_status, name='reset_status'),
]
