from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^catalogues$', views.catalogues, name='catalogues'),
    url(r'^catalogue_stored$', views.catalogue_stored, name='catalogue_stored'),
    url(r'^index2$', views.index2, name='index2'),
]