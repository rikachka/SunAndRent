from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^catalogues$', views.catalogues, name='catalogues'),
    url(r'^catalogue_goods$', views.catalogue_goods, name='catalogue_goods'),
    url(r'^catalogue_stored$', views.catalogue_stored, name='catalogue_stored'),
    url(r'^catalogue_rented$', views.catalogue_rented, name='catalogue_rented'),
    url(r'^return_good_to_owner/(?P<item_pk>[0-9]+)$', views.return_good_to_owner, name='return_good_to_owner'),
]